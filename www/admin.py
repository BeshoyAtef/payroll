from django.contrib import admin
from www.models import *
import datetime
from datetime import date
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect, HttpResponse

def make_published(modeladmin, request, queryset):
    current_month = date.today()
    list_of_slips = []
    list_of_exceptions = []
    total_payments = 0
    for employee in queryset:
        try:
            paymentlist = Payment.objects.filter(employee=employee)
            payment = paymentlist.get(date__month = current_month.month)
            list_of_slips.append(payment)
            total_payments = total_payments + payment.amount

        except:
            list_of_exceptions.append(employee)

    return render_to_response('paymentslip.html', {'list_of_exceptions':list_of_exceptions,'slips_list': list_of_slips, 'month':current_month})
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


