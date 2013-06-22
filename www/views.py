from www.models import *
from django.http import HttpResponse
import simplejson
from django.shortcuts import render_to_response, redirect, render
from django.http import *
from django.shortcuts import render_to_response, redirect, render
from django.core.urlresolvers import reverse
from www.models import *
from django.core.context_processors import csrf
from django.template import RequestContext   
from django.utils import simplejson     
import json 
def index(request):
    return HttpResponse(" <a href='/admin'>Click here to got o the admin page</a>")

def import_attendance(request):
    return HttpResponse(" <h1>Welcome to the Attendance upload page</h1> ")

def view_reports(request):
    return HttpResponse(" <h1>Welcome to thereports page</h1> ")


def goToCompanyReports(request):
	return render(request, 'companyReports.html')


def view_output_yearly(request):
	values = []
	keys = []
	content = ""
	desired_year = request.GET['year']
	Dict = company_wide_output_yearly_report(int(desired_year))
	Dict = simplejson.dumps(Dict)
	return HttpResponse(Dict)


def company_wide_salaryReport(request):
	# t = "2013"
	desired_year = request.GET['year']
	Dict =  company_wide_output_yearly_report(int(t))
	Dict = simplejson.dumps(Dict)
	return HttpResponse(Dict)

def view_output_monthly(request):
	values = []
	keys = []
	content = ""
	desired_year = request.GET['year']
	desired_month = request.GET['month']
	Dict = company_wide_output_monthly_report(int(desired_year),int(desired_month))
	Dict = simplejson.dumps(Dict)
	return HttpResponse(Dict)


def company_wide_output_monthlyReport(request):
	desired_year = request.GET['year']
	desired_month = request.GET['month']
	Dict = company_wide_output_monthly_report(int(desired_year), int(desired_month))
	return render(request,'companyReports.html', Dict)

def company_wide_output_yearlyReport(request):
	desired_year = request.GET['year']
	print desired_year
	Dict = company_wide_output_yearly_report(int(desired_year))
	Dict = simplejson.dumps(Dict)
	print Dict
	return HttpResponse(Dict)

def company_wide_yearly_attendanceReport(request):
	desired_year = request.POST['year']
	Dict = company_wide_yearly_attendance_report(desired_year)
	return render(request,'companyReports.html', Dict)


def company_wide_monthly_attendanceReport(request):
	desired_year = request.POST['year']
	desired_month = request.POST['month']
	print desired_year
	print desired_month
	Dict = company_wide_monthly_attendance_report(int(desired_year), int(desired_month))
	return render(request,'companyReports.html', Dict)
	
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

