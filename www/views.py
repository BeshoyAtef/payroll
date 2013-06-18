# Create your views here.

from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from www.models import *
from django.shortcuts import render_to_response, redirect, render
from django.core.context_processors import csrf
from django.template import RequestContext        

def index(request):
    return HttpResponse(" <a href='/admin'>Click here to got o the admin page</a>")

def import_attendance(request):
    return HttpResponse(" <h1>Welcome to the Attendance upload page</h1> ")

def view_reports(request):
    return HttpResponse(" <h1>Welcome to thereports page</h1> ")



flag_done=False
def add_batch(request):
    global flag_done
    if request.method == "GET" :
        batches=Batch.objects.all()
        employees=Employee.objects.all()
        items=Item.objects.all()
        flag=flag_done
        flag_done=False
        return render_to_response('rapid_batch.html', {'batch_list':batches,'employee_list': employees, 'item_list':items,'flag_done':flag}, context_instance=RequestContext(request))
    else :
        employee_id = request.POST['employee']
        tmp_date = request.POST['date']
        item_id = request.POST['identifier']
        tmp_item_price = request.POST['item_price']
        tmp_size = request.POST['size']
        tmp_reason = request.POST['reason']
        tmp_employee = Employee.objects.get(id=employee_id)
        tmp_item = Item.objects.get(id=item_id)
        batch = Batch(employee=tmp_employee,date=tmp_date,item=tmp_item,item_price=tmp_item_price,size=tmp_size,
            reason=tmp_reason)
        flag_done=True
        batch.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

