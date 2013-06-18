# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse(" <a href='/admin'>Click here to got o the admin page</a>")

def import_attendance(request):
    return HttpResponse(" <h1>Welcome to the Attendance upload page</h1> ")

def view_reports(request):
    return HttpResponse(" <h1>Welcome to thereports page</h1> ")


def company_wide_salary_report(request):
	desired_year = request.GET['year']
	Dict = company_wide_salary_report(desired_year)
	return render(request, Dict)

def company_wide_output_yearly_report(request):
	desired_year = request.GET['year']
	Dict = company_wide_output_yearly_report(desired_year)
	return render(request, Dict)

def company_wide_output_monthly_report(request):
	desired_year = request.GET['year']
	desired_month = request.GET['month']
	Dict = company_wide_output_monthly_report(desired_year, desired_month)
	return render(request, Dict)

def company_wide_yearly_attendance_report(request):
	desired_year = request.GET['year']
	Dict = company_wide_yearly_attendance_report(desired_year)
	return render(request, Dict)

def company_wide_monthly_attendance_report(request):
	desired_year = request.GET['year']
	desired_month = request.GET['month']
	Dict = company_wide_monthly_attendance_report(desired_year, desired_month)
	return render(request, Dict)
	