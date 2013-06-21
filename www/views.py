# Create your views here.
# Full path and name to the csv file
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import re
import csv
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponse
from www.forms import UploadForm
from django.template import RequestContext
from www.models import CsvFile
from www.models import Attendance , Employee

from payroll import settings
from payroll.settings import MEDIA_ROOT
import csv
import string 
import datetime

def index(request):
    return HttpResponse(" <a href='/admin'>Click here to got o the admin page</a>")

def import_attendance(request):
    return HttpResponse(" <h1>Welcome to the Attendance upload page</h1> ")

def view_reports(request):
    return HttpResponse(" <h1>Welcome to thereports page</h1> ")


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            fileup= form.cleaned_data['file']
            temp = CsvFile.objects.create(attendence_sheet=fileup)
            print temp.attendence_sheet
            
            # path = media/temp.attendence_sheet.url

            
            dataReader = csv.reader(open('%s/%s' % (MEDIA_ROOT, temp.attendence_sheet)), delimiter=',', quotechar='"')
            
            dic = {}
            for row in dataReader:
                if row[0] != 'Ac-No': # Ignore the header row, import everything else
                    account_number = row[0]
                    stime = row[2]
                    if account_number not in dic:
                        dic[account_number] = []

                    dic[account_number].append(stime)

            for acc, stimes in dic.iteritems():


                checkin = stimes.pop(0)
                
                employee = Employee.objects.get(acc_no= acc)
                # print str(employee.acc_no)
                
                
                d = checkin[:-4].strip()
                check_in = datetime.datetime.strptime(d, "%m/%d/%Y %H:%M" )
                
                check_out = None
                for stime in stimes:
                   
                    stime = stime[:-4].strip()
                    stime = datetime.datetime.strptime(stime, "%m/%d/%Y %H:%M" )
                    
                    if stime.date() == check_in.date():
                        check_out = stime
                        
                    

                    else:
                        
                        if not Attendance.objects.filter(check_in=check_in,check_out=check_out,employee=employee).exists():
                            attend = Attendance()
                            attend.check_in = check_in
                            attend.check_out = check_out
                            attend.employee = employee
                            attend.save()
                            check_in = stime
                            check_out= None
                        else:
                            return HttpResponse ("file has been read")

                attend = Attendance()
                attend.check_in = check_in
                attend.check_out = check_out
                attend.employee = employee
                attend.save()
                check_in = stime
                check_out= None

            return HttpResponse('sucess')
        else :
            return render_to_response('upload.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = UploadForm()
        context = {'form': form}
        return render_to_response('upload.html', context, context_instance=RequestContext(request))

