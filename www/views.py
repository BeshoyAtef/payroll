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
