# Create your views here.
from www.models import *
from django.http import HttpResponse
import simplejson
from django.shortcuts import render_to_response, redirect, render

def index(request):
    return HttpResponse(" <a href='/admin'>Click here to got o the admin page</a>")

def import_attendance(request):
    return HttpResponse(" <h1>Welcome to the Attendance upload page</h1> ")

def view_reports(request):
    return HttpResponse(" <h1>Welcome to thereports page</h1> ")

def goToCompanyReports(request):
	return render(request, 'companyReports.html')

def company_wide_salaryReport(request):
	desired_year = request.GET['year']
	Dict =  company_wide_salary_report(int(desired_year))
	# dicto = simplejson.dumps(Dict)
	return render(request,'companyReports.html', Dict)

def company_wide_output_yearlyReport(request):
	desired_year = request.POST['year']
	print desired_year
	Dict = company_wide_output_yearly_report(int(desired_year))
	return render(request,'companyReports.html', Dict)

def company_wide_yearly_attendanceReport(request):
	desired_year = request.POST['year']
	Dict = company_wide_yearly_attendance_report(desired_year)
	return render(request,'companyReports.html', Dict)

def company_wide_output_monthlyReport(request):
	desired_year = request.POST['year']
	desired_month = request.POST['month']
	Dict = company_wide_output_monthly_report(int(desired_year), int(desired_month))
	return render(request,'companyReports.html', Dict)

def company_wide_monthly_attendanceReport(request):
	desired_year = request.POST['year']
	desired_month = request.POST['month']
	print desired_year
	print desired_month
	Dict = company_wide_monthly_attendance_report(int(desired_year), int(desired_month))
	return render(request,'companyReports.html', Dict)
	