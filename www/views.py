<<<<<<< HEAD
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
=======
from django.http import *
from django.shortcuts import render_to_response, redirect, render
from django.core.urlresolvers import reverse
from www.models import *
from django.core.context_processors import csrf
from django.template import RequestContext   
from django.utils import simplejson     
import json 
>>>>>>> master

def index(request):
    return HttpResponse(" <a href='/admin'>Click here to got o the admin page</a>")

def import_attendance(request):
    return HttpResponse(" <h1>Welcome to the Attendance upload page</h1> ")

def view_reports(request):
    return HttpResponse(" <h1>Welcome to thereports page</h1> ")


<<<<<<< HEAD
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

            return HttpResponse('sucess')
        else :
            return render_to_response('upload.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = UploadForm()
        context = {'form': form}
        return render_to_response('upload.html', context, context_instance=RequestContext(request))

=======
# can be deleted
# can be deleted
# can be deleted

def add_batch(request):
    global flag_done
    if request.method == "GET" :
        batches=Batch.objects.all()
        employees=Employee.objects.all()
        items=Item.objects.all()
        flag=flag_done
        flag_done=False
        print batches
        batches.order_by('pub_date')
        print batches
        return render_to_response('rapid_batch.html', {'batch_list':batches,'employee_list': employees, 'item_list':items,'flag_done':flag}, context_instance=RequestContext(request))
    else :
        employee_id = request.POST['employee']
        tmp_date = request.POST['date']
        item_id = request.POST['identifier'] 
        tmp_size = request.POST['size']
        tmp_reason = request.POST['reason']
        tmp_employee = Employee.objects.get(id=employee_id)
        tmp_item = Item.objects.get(id=item_id)
        if 'item_price' not in request.POST: #to handel if the price didt change by the user
            tmp_item_price = tmp_item.value
        else :
            tmp_item_price = request.POST['item_price']
        batch = Batch(employee=tmp_employee,date=tmp_date,item=tmp_item,item_price=tmp_item_price,size=tmp_size,
            reason=tmp_reason)
        flag_done=True
        print batch
        batch.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def view_page(request):
	content = "Here the report content should go like this is a report of the employee productivity etc.."
	return render_to_response('test.html',{'content':content})

def dummy_method(request):
	data = [{'a': '10'},{'b':'20'},{'c':'7'}]
	return HttpResponse(simplejson.dumps(data))
>>>>>>> master
