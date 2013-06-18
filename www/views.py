# Create your views here.

from django.http import HttpResponse

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
	total_hours = employee.working_hours(year, month, 1, year, month+1, 1, "fixed")
	productivity = employee.productivity(year, month, 1, year, month+1, 1, "fixed")
	average_productivity = productivity/total_hours
	return render(request, '', {'average_productivity': average_productivity})

#Mohamed Awad
#this def calculates the employee average prductivity per year
#the def takes as request the specific year the admin is wishing to look for
#and returns all products produced by such employee divided by the total hours he worked in that year
def employee_productivity_year(request):
	year = request.GET['year']
	employee = Employee.objects.get(id = request.GET['employee'])
	total_hours = employee.working_hours(year, 1, 1, year+1, 1, 1, "fixed")
	productivity = employee.productivity(year, 1, 1, year+1, 1, 1, "fixed")
	average_productivity = productivity/total_hours
	return render(request, '', {'average_productivity': average_productivity})

#Mohamed Awad
#this def calculates the employee average prductivity per any range of time
#the def takes as request the specific start year, start month, start day, end year, end month and end day 
#the admin is wishing to look for
#and returns all products produced by such employee divided by the total hours he worked in that specific range of time
def employee_productivity_custom(request):
	month_start = request.GET['month_start']
	year_start = request.GET['year_start']
	day_start = request.GET['day_start']
	month_end = request.GET['month_end']
	year_end = request.GET['year_end']
	day_end = request.GET['day_end']	
	employee = Employee.objects.get(id = request.GET['employee'])
	total_hours = employee.working_hours(year_start, month_start, day_start, year_end, month_end, day_end, "custom")
	productivity = employee.productivity(year_start, month_start, day_start, year_end, month_end, day_end, "custom")
	average_productivity = productivity/total_hours
	return render(request, '', {'average_productivity': average_productivity})

#Mohamed Awad
#this def calculates the employee payement in a specific yaer
#the def takes as request the specific year the admin is wishing to look for
#and returns total payements the employee received or will receive
#in that specific year
def employee_payement_year(request):
	year = request.GET['year']
	employee = Employee.objects.get(id = request.GET['employee'])
	total_hours = employee.payement(year, 1, 1, year+1, 1, 1)
	return render(request, '', {'average_productivity': average_productivity})

#Mohamed Awad
#this def calculates the employee payement in a specific month
#the def takes as request the specific year and month the admin is wishing to look for
#and returns total payements the employee received or will receive
#in that specific month
def employee_payement_month(request):
	year = request.GET['year']
	month = request.GET['month']
	employee = Employee.objects.get(id = request.GET['employee'])
	total_hours = employee.payement(year, month, 1, year, month+1, 1)
	return render(request, '', {'average_productivity': average_productivity})