
from django.http import *
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
from www.models import *
from datetime import date
import json
from django.utils import simplejson
from django.core import serializers
from django.template import RequestContext, Template

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

# def calc_attendance_month(month, year, employee):
# 	days = -((date(year, month, 1) - date(year, month+1, 1)).days)
# 	number_of_attendances = employee.attendances_monthly(year, month, 1, year, month + 1, 1)
# 	return (number_of_attendances/float(days))*100

# def employee_attendance_month(request):
# 	month = int(request.GET['month'])
# 	year = int(request.GET['year'])
# 	employee = Employee.objects.get(pk = int(request.GET['e_id']))
# 	return HttpResponse(json.dumps({'attendance_percentage': str(calc_attendance_month(month,year,employee))}))

# def employe_attendance_year(request):
# 	year = int(request.GET['year'])
# 	employee = Employee.objects.get(pk = int(request.GET['e_id']))
# 	months = 1
# 	total_attendance_percentage = []
# 	while months < 12:
# 		attendance_percentage = calc_attendance_month(months, year, employee)
# 		months = months + 1
# 		att_dict = {'attendance_percentage': str(attendance_percentage)}
# 		total_attendance_percentage.append(attendance_percentage)
# 	return HttpResponse(json.dumps(total_attendance_percentage))

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

def view_page(request):
	content = "Here the report content should go like this is a report of the employee productivity etc.."
	return render_to_response('test.html',{'content':content})

def dummy_method(request):
	data = [{'a': '10'},{'b':'20'},{'c':'7'}]
	return HttpResponse(simplejson.dumps(data))