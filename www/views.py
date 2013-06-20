# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, render
from www.models import *
from datetime import date
import json
from django.utils import simplejson
from django.core import serializers

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
	print "yyyyyyyyyyyyyyyy"
	print int(request.GET['month'])
	employee = Employee.objects.get(id = int(request.GET['e_id']))
	days = -((date(year, month, 1) - date(year, month+1, 1)).days)
	average_productivity_array = []
	iterator = 1
	while iterator <= days :
		total_hours = employee.working_hours(year, month, iterator, year, month, iterator + 1, "custom")
		productivity = employee.productivity(year, month, iterator, year, month, iterator + 1, "custom")
		print "testing"
		print productivity
		print total_hours
		iterator = iterator + 1
		try:
			average_productivity = productivity/total_hours
			average_productivity_array.append(average_productivity)
		except:
			average_productivity_array.append(0)
		iterator = iterator + 1
	print "productivity month"
	print average_productivity_array
	return render(request, '', {'average_productivity_array': average_productivity_array})

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
		total_hours = employee.working_hours(year, months, 1, year, months+1, 1, "custom")
		productivity = employee.productivity(year, months, 1, year, months+1, 1, "custom")
		print "yyyyyyyyyy"
		print productivity
		print total_hours
		try:
			average_productivity = productivity/total_hours
			average_productivity_array.append(average_productivity)
		except:
			average_productivity_array.append(0)
		months = months + 1
	print "productivity year"
	print average_productivity_array
	return render(request, '', {'average_productivity_array': average_productivity_array})

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
		total_payements_array.append(total_payements)
		months = months + 1
	print "payement year"
	print total_payements_array
	return render(request, '', {'total_payements_array': total_payements_array})

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
		payement_array.append(total_payement)
	last_day_payement = payement_array[-1]
	last_day_payement = last_day_payement + employee.salary
	payement_array[-1] = last_day_payement
	return render(request, '', {'payement_array': payement_array})

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
		payement_array.append(total_hours)
	return render(request, '', {'workinghours_array': workinghours_array})

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
		total_hours = employee.working_hours(year, months, 1, year, months+1, 1, "custom")
		months = months + 1
		total_hours_array.append(total_hours)
	return render(request, '', {'total_hours_array': total_hours_array})