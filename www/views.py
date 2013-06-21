
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
	print "done"
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
	while iterator < days:
		total_payement = employee.payement_monthly(year, month, iterator, year, month, iterator + 1)
		iterator = iterator + 1
		pay_dict = {str(iterator): str(total_payement)}
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
	while iterator < days:
		total_hours = employee.working_hours(year, month, iterator, year, month, iterator + 1, "custom")
		iterator = iterator + 1
		hrs_dict = {str(iterator): str(total_hours)}
		payement_array.append(total_hours)
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
		months = months + 1
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
		total_days = get_total_days(year, months, days)
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
   	response = HttpResponse(json.dumps(total_abscence_array))
	return response

def get_total_days(year, month, days):
	day = 1
	total_days = 0
	while day < days:
		print "in while"
		date = datetime.date(year, month, day).strftime("%A")
		if  date != 'Sunday':
			total_days = total_days + 1
		day = day + 1
	return total_days

def products_month(request):
	month = int(request.GET['month'])
	year = int(request.GET['year'])
	employee = Employee.objects.get(pk = int(request.GET['e_id']))
	workinghours_array = []
	iterator = 1
	days = -((date(year, month, 1) - date(year, month+1, 1)).days)
	products_array = []
	while iterator < days:
		products = employee.productivity(year, month, iterator, year, month, iterator + 1, "custom")
		iterator = iterator + 1
		prd_dict = {str(iterator): str(products)}
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
		months = months + 1
		prd_dict = {str(months): str(total_products)}
		total_products_array.append(prd_dict)
	print "look here"
	print total_products_array
   	response = HttpResponse(json.dumps(total_products_array))
	return response
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
