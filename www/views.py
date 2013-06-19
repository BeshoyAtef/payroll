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
	month = request.GET['month']
	year = request.GET['year']
	employee = Employee.objects.get(id = request.GET['employee'])
	days = -((date(year, month, 1) - date(year, month+1, 1)).days)
	average_productivity_array = []
	iterator = 1
	while iterator <= days :
		total_hours = employee.working_hours(year, month, days, year, month, iterator, "custom")
		productivity = employee.productivity(year, month, days, year, month, iterator, "custom")		
		average_productivity = len(productivity)/total_hours
		average_productivity_array.append(average_productivity)
		iterator = iterator + 1
	return render(request, '', {'average_productivity_array': average_productivity_array})

#Mohamed Awad
#this def calculates the employee average prductivity per year
#the def takes as request the specific year the admin is wishing to look for
#and returns all products produced by such employee divided by the total hours he worked in that year
def employee_productivity_year(request):
	year = request.GET['year']
	employee = Employee.objects.get(id = request.GET['employee'])
	average_productivity_array = []
	months = 1
	while months < 12:
		total_hours = employee.working_hours(year, months, 1, year, months+1, 1, "custom")
		productivity = employee.productivity(year, months, 1, year, months+1, 1, "custom")	
		average_productivity = len(productivity)/total_hours
		average_productivity_array.append(average_productivity)
	return render(request, '', {'average_productivity_array': average_productivity_array})

#Mohamed Awad
#this def calculates the employee payement in a specific yaer
#the def takes as request the specific year the admin is wishing to look for
#and returns total payements the employee received or will receive
#in that specific year
def employee_payement_year(request):
	year = request.GET['year']
	employee = Employee.objects.get(id = request.GET['employee'])
	months = 1
	total_payements = []
	while months < 12:
		total_payements = employee.payement(year, months, 1, year, months+1, 1, "custom")
		total_payements.append(total_payements)
	return render(request, '', {'total_payements': total_payements})

#Mohamed Awad
#this def calculates the employee payement in a specific month
#the def takes as request the specific year and month the admin is wishing to look for
#and returns total payements the employee received or will receive
#in that specific month
def employee_payement_month(request):
	year = request.GET['year']
	month = request.GET['month']
	employee = Employee.objects.get(id = request.GET['employee'])
	days = -((date(year, month, 1) - date(year, month+1, 1)).days)
	payement_array = []
	iterator = 1
	while iterator <= days:
		total_payement = employee.payement(year, month, days, year, month, iterator, "custom")
		iterator = iterator + 1	
		payement_array.append(total_payement)
	return render(request, '', {'payement_array': payement_array})

def view_report_page(request):
	employees =  Employee.objects.all()
	print employees
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
		iterator = iterator + 1	
		print "in view"
		payement_array.append(total_hours)
	return render(request, '', {'workinghours_array': workinghours_array})

#Mohamed Awad
#this def calculates the employee average prductivity per year
#the def takes as request the specific year the admin is wishing to look for
#and returns all products produced by such employee divided by the total hours he worked in that year
def employee_workinghours_year(request):
	year = request.GET['year']
	employee = Employee.objects.get(id = request.GET['employee'])
	months = 1
	total_hours_array = []
	while months < 12:
		total_hours = employee.working_hours(year, months, 1, year, months+1, 1, "custom")
		months = months + 1
		total_hours_array.append()
	return render(request, '', {'total_hours_array': total_hours_array})