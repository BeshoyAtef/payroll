# Create your views here.

from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from www.models import *

def index(request):
    return HttpResponse(" <a href='/admin'>Click here to got o the admin page</a>")

def import_attendance(request):
    return HttpResponse(" <h1>Welcome to the Attendance upload page</h1> ")

def view_reports(request):
    return HttpResponse(" <h1>Welcome to thereports page</h1> ")

def add_batch(request):
    employee_id = request.POST['employee']
    tmp_date = request.POST['date']
    item_id = request.POST['identifier']
    tmp_item_price = request.POST['item_price']
    tmp_size = request.POST['size']

    tmp_employee = Employee.objects.get(id=employee_id)
    tmp_item = Item.objects.get(id=item_id)

    batch = Batch(employee=tmp_employee,date=tmp_date,item=tmp_item,item_price=tmp_item_price,size=tmp_size)
    batch.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

