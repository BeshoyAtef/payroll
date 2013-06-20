from django.http import *
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
import json 
from django.utils import simplejson
def index(request):
    return HttpResponse(" <a href='/admin'>Click here to got o the admin page</a>")

def import_attendance(request):
    return HttpResponse(" <h1>Welcome to the Attendance upload page</h1> ")

def view_reports(request):
    return HttpResponse(" <h1>Welcome to thereports page</h1> ")
def view_page(request):
	content = "Here the report content should go like this is a report of the employee productivity etc.."
	return render_to_response('test.html',{'content':content})

def dummy_method(request):
	data = [{'a': '10'},{'b':'20'},{'c':'7'}]
	return HttpResponse(simplejson.dumps(data))