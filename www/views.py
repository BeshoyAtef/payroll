# Create your views here.
# Full path and name to the csv file
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


import csv
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponse
from www.forms import UploadForm
from django.template import RequestContext
from www.models import CsvFile
def index(request):
    return HttpResponse(" <a href='/admin'>Click here to got o the admin page</a>")

def import_attendance(request):
    return HttpResponse(" <h1>Welcome to the Attendance upload page</h1> ")

def view_reports(request):
    return HttpResponse(" <h1>Welcome to thereports page</h1> ")


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            fileup= form.cleaned_data['file']
            CsvFile.objects.create(attendence_sheet=fileup)




            # reading file ...
            return HttpResponse('sucess')
        else :
            return render_to_response('upload.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = UploadForm()
        context = {'form': form}
        return render_to_response('upload.html', context, context_instance=RequestContext(request))

