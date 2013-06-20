from django.contrib import admin
from www.views import import_attendance
from django.http import HttpResponse
from www.models import *
import datetime
from datetime import date
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from admin_views.admin import AdminViews
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

def show_employee_reports(modeladmin, request, queryset):
    current_year = datetime.datetime.now().year
    years = []
    while current_year != 1999:
        years.append(current_year)
        current_year = current_year - 1
    return render(request, 'reportPage.html', {'employees': queryset, 'years': years})
show_employee_reports.short_description = "show reports"

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','mobile', 'ssn']
    search_fields = ['name', 'email','mobile', 'ssn']
    actions = [make_published,show_employee_reports]

def my_view(request, *args, **kwargs):
    return HttpsResponse(" <a href='/admin'>here to do nothing</a>")

class TestAdmin(AdminViews):
    admin_views = (
                    ('Test Report', 'redirect_to_cnn'),
                    ('Upload Attendance-Log','import_attendance'),
        )

    def redirect_to_cnn(self, *args, **kwargs):
        return HttpResponse(" <a href='/admin'>here to do nothing</a>")

admin.site.register(Item, TestAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Batch)
admin.site.register(Payment)
admin.site.register(Loan)
admin.site.register(CompanyDowntime)

#remove unneeded items 
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
