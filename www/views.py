# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse(" <a href='/admin'>Click here to got o the admin page</a>")

def import_attendance(request):
    return HttpResponse(" <h1>Welcome to the Attendance upload page</h1> ")

def view_reports(request):
    return HttpResponse(" <h1>Welcome to thereports page</h1> ")

def add_batch(request):
    employee_id = request.POST['employee']
    date = request.POST['date']
    item_id = request.POST['identifier']
    item_price = request.POST['item_price']
    size = request.POST['size']
    return HttpResponse(" <h1>i got the info</h1> ")


