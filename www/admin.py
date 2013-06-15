from django.contrib import admin
from www.models import *
import datetime
from datetime import date
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect, HttpResponse

def make_published(modeladmin, request, queryset):
    current_month = date.today().month
    list_of_slips = []
    for employee in queryset:
        try:
            payment = Payment.objects.get(employee = employee)
            list_of_slips.append(payment)
        except:
            pass
    return render_to_response('test.html', {'slips_list': list_of_slips})
make_published.short_description = "Print payment slips"

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','mobile', 'ssn']
    search_fields = ['name', 'email','mobile', 'ssn']
    actions = [make_published]

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Batch)
admin.site.register(Payment)
admin.site.register(Loan)
admin.site.register(CompanyDowntime)
admin.site.register(Item)


