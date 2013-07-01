# Create your views here.
# Full path and name to the csv file
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import re

from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect, HttpResponse

from www.forms import UploadForm
from django.template import RequestContext
from payroll import settings
from payroll.settings import MEDIA_ROOT
import csv
import string 
import datetime
from django.http import *
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
from www.models import *
from datetime import date
import json
from django.utils import simplejson
from django.core import serializers
from django.template import RequestContext, Template
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.utils import simplejson


def index(request):
    return HttpResponse(" <a href='/admin'>Click here to got o the admin page</a>")

def import_attendance(request):
    return HttpResponse(" <h1>Welcome to the Attendance upload page</h1> ")

def view_reports(request):
    return HttpResponse(" <h1>Welcome to thereports page</h1> ")

def switch_lang(request):
    if request.session['django_language'] == 'en': 
        request.session['django_language'] = 'ar'
    else:
        request.session['django_language'] = 'en'
    return redirect('index.html')


#Mohamed Awad
#this def calculates the employee average prductivity per month
#the def takes as request the desired month and year the admin is wishing to look for
#and returns all products produced by such employee divided by the total hours he worked in that month
def employee_productivity_month(request):
	month = int(request.GET['month'])
	year = int(request.GET['year'])
	employee = Employee.objects.get(id = int(request.GET['e_id']))
	days = -((date(year, month, 1) - date(year, month+1, 1)).days)
	average_productivity_array = []
	iterator = 1
	while iterator <= days :
		total_hours = float(employee.working_hours(year, month, iterator, year, month, iterator, "custom"))
		productivity = float(employee.productivity(year, month, iterator, year, month, iterator, "custom"))
		try:
			average_productivity = productivity/total_hours
			avg_dict = {str(iterator): str(average_productivity)}
			average_productivity_array.append(avg_dict)
		except:
			average_productivity_array.append({str(iterator):'0'})
		iterator = iterator + 1
	return HttpResponse(json.dumps(average_productivity_array))

#Mohamed Awad
#this def calculates the employee average prductivity per year
#the def takes as request the specific year the admin is wishing to look for
#and returns all products produced by such employee divided by the total hours he worked in that year
def employee_productivity_year(request):
	print "done caching"
	year = int(request.GET['year'])
	employee = Employee.objects.get(id = int(request.GET['e_id']))
	average_productivity_array = []
	months = 1
	while months < 12:
		total_hours = employee.working_hours(year, months, 1, year, months+1, 1, "fixed")
		productivity = employee.productivity(year, months, 1, year, months+1, 1, "fixed")
		try:
			average_productivity = float(productivity)/float(total_hours)
			avg_dict = {str(months): str(average_productivity)}
			average_productivity_array.append(avg_dict)
		except:
			average_productivity_array.append({str(months): '0'})
		months = months + 1
		if months == 12:
			total_hours = employee.working_hours(year, months, 1, year+1, 1, 1, "fixed")
			productivity = employee.productivity(year, months, 1, year+1, 1, 1, "fixed")
			try:
				average_productivity = float(productivity)/float(total_hours)
				avg_dict = {str(months): str(average_productivity)}
				average_productivity_array.append(avg_dict)
			except:
				average_productivity_array.append({str(months): '0'})
	return HttpResponse(json.dumps(average_productivity_array))

#Mohamed Awad
#this def calculates the employee payement in a specific yaer
#the def takes as request the specific year the admin is wishing to look for
#and returns total payements the employee received or will receive
#in that specific year
def employee_payement_year(request):
	year = int(request.GET['year'])
	employee = Employee.objects.get(id = int(request.GET['e_id']))
	months = 1
	total_payements_array = []
	while months < 12:
		total_payements = employee.payement_yearly(year, months, 1, year, months+1, 1)
		pay_dict = {str(months): str(total_payements)}
		total_payements_array.append(pay_dict)
		months = months + 1
		if months == 12:
			total_payements = employee.payement_yearly(year, months, 1, year+1, 1, 1)
			pay_dict = {str(months): str(total_payements)}
			total_payements_array.append(pay_dict)
	print total_payements_array
	return HttpResponse(json.dumps(total_payements_array))

#Mohamed Awad
#this def calculates the employee payement in a specific month
#the def takes as request the specific year and month the admin is wishing to look for
#and returns total payements the employee received or will receive
#in that specific month
def employee_payement_month(request):
	year = int(request.GET['year'])
	month = int(request.GET['month'])
	employee = Employee.objects.get(id = int(request.GET['e_id']))
	days = -((date(year, month, 1) - date(year, month+1, 1)).days)
	payement_array = []
	iterator = 1
	while iterator <= days:
		total_payement = employee.payement_monthly(year, month, iterator, year, month, iterator)
		pay_dict = {str(iterator): str(total_payement)}
		iterator = iterator + 1
		payement_array.append(pay_dict)
	last_day_payement = int(payement_array[-1].values()[0])
	last_day_payement = last_day_payement + employee.salary
	payement_array[-1] = {str(iterator): str(last_day_payement)}
	return HttpResponse(json.dumps(payement_array))

def view_report_page(request):
	employees =  Employee.objects.all()
	return render(request, 'reportPage.html', {'employees': employees})

#Mohamed Awad
#this def calculates the employee average prductivity per month
#the def takes as request the desired month and year the admin is wishing to look for
#and returns all products produced by such employee divided by the total hours he worked in that month
def employee_workinghours_month(request):
	month = int(request.GET['month'])
	year = int(request.GET['year'])
	employee = Employee.objects.get(pk = int(request.GET['e_id']))
	workinghours_array = []
	iterator = 1
	days = -((date(year, month, 1) - date(year, month+1, 1)).days)
	payement_array = []
	while iterator <= days:
		total_hours = employee.working_hours(year, month, iterator, year, month, iterator, "custom")
		hrs_dict = {str(iterator): str(total_hours)}
		iterator = iterator + 1
		payement_array.append(hrs_dict)
	return HttpResponse(json.dumps(payement_array))

#Mohamed Awad
#this def calculates the employee average prductivity per year
#the def takes as request the specific year the admin is wishing to look for
#and returns all products produced by such employee divided by the total hours he worked in that year
def employee_workinghours_year(request):
	year = int(request.GET['year'])
	employee = Employee.objects.get(pk = int(request.GET['e_id']))
	months = 1
	total_hours_array = []
	while months < 12:
		total_hours = employee.working_hours(year, months, 1, year, months+1, 1, "fixed")
		hrs_dict = {str(months): str(total_hours)}
		months = months + 1
		total_hours_array.append(hrs_dict)
		if months == 12:
			total_hours = employee.working_hours(year, months, 1, year+1, 1, 1, "fixed")
			hrs_dict = {str(months): str(total_hours)}
			total_hours_array.append(hrs_dict)			
   	response = HttpResponse(json.dumps(total_hours_array))
	return response

#Mohamed Awad
#this def calculates the employee average prductivity per year
#the def takes as request the specific year the admin is wishing to look for
#and returns all products produced by such employee divided by the total hours he worked in that year
def employee_abscence_year(request):
	year = int(request.GET['year'])
	employee = Employee.objects.get(pk = int(request.GET['e_id']))
	months = 1
	total_abscence_array = []
	while months < 12:
		days = (date(year, months+1, 1) - date(year, months, 1)).days
		total_attendances = get_total_days(year, months, days, employee)
		attendances_dict = {str(months):str(total_attendances)}
		total_abscence_array.append(attendances_dict)
		months = months + 1
		#the following lines are not used bs msh hashelha 3alashan te3ebt feehom fa fakes
		# days = (date(year, months+1, 1) - date(year, months, 1)).days
		# print days
        # date_start = datetime.datetime(year, months, 1)
        # date_end = datetime.datetime(year, months, days)
        # print date_start
        # print date_end
        # print "look"
        # working_days = workdaysub(date_start, date_end)
        # print working_days
        # months = months + 1
        # abs_dict = {str(months): str(total_hours)}
        # total_abscence_array.append(abs_dict)
        if months == 12:
			days = 31
			total_attendances = get_total_days(year, months, days, employee)
			attendances_dict = {str(months):str(total_attendances)}
			total_abscence_array.append(attendances_dict)
   	response = HttpResponse(json.dumps(total_abscence_array))
	return response

def get_total_days(year, month, days, employee):
	day = 1
	total_attendances = 0
	while day < days:
		date = datetime.date(year, month, day).strftime("%A")
		if  date != 'Sunday':
			total_attendances = total_attendances + len(employee.get_attendance(year, month, day, year, month, day))
		day = day + 1
	return total_attendances

def products_month(request):
	month = int(request.GET['month'])
	year = int(request.GET['year'])
	employee = Employee.objects.get(pk = int(request.GET['e_id']))
	workinghours_array = []
	iterator = 1
	days = -((date(year, month, 1) - date(year, month+1, 1)).days)
	products_array = []
	while iterator <= days:
		products = employee.productivity(year, month, iterator, year, month, iterator, "custom")
		prd_dict = {str(iterator): str(products)}
		iterator = iterator + 1
		products_array.append(prd_dict)
	return HttpResponse(json.dumps(products_array))

#Mohamed Awad
#this def calculates the employee average prductivity per year
#the def takes as request the specific year the admin is wishing to look for
#and returns all products produced by such employee divided by the total hours he worked in that year
def products_year(request):
	year = int(request.GET['year'])
	employee = Employee.objects.get(pk = int(request.GET['e_id']))
	months = 1
	total_products_array = []
	while months < 12:
		total_products = employee.productivity(year, months, 1, year, months+1, 1, "fixed")
		prd_dict = {str(months): str(total_products)}
		months = months + 1
		total_products_array.append(prd_dict)
		if months == 12:
			total_products = employee.productivity(year, months, 1, year+1, 1, 1, "fixed")
			prd_dict = {str(months): str(total_products)}
			total_products_array.append(prd_dict)
   	response = HttpResponse(json.dumps(total_products_array))


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
>>>>>>> master


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

