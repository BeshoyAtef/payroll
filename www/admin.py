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
    attendance = Attendance.objects.all()
    return render_to_response('paymentslip.html', {'attendance':attendance,'list_of_exceptions':list_of_exceptions,'slips_list': list_of_slips, 'month':current_month})
make_published.short_description = "Print payment slips"

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','mobile', 'ssn']
    search_fields = ['name', 'email','mobile', 'ssn']
    actions = [make_published]
    list_filter = ('salary',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        employee=Employee.objects.get(id=object_id)
        batches=Batch.objects.filter(employee=employee)
        attendance=Attendance.objects.filter(employee=employee)
        print attendance

        extra_context = {'batch_list':batches,'attendance_list':attendance}

        return super(EmployeeAdmin, self).change_view(request, object_id,
            form_url, extra_context=extra_context)


# class BatchAdmin(admin.ModelAdmin):


#     list_display = ['id','employee', 'date','item', 'item_price','size','reason']
#     search_fields = ['employee__name', 'date','item__identifier', 'item_price','size','reason']

#     def changelist_view(self, request, extra_context=None):
#         batches=Batch.objects.all()
#         employees=Employee.objects.all()
#         items=Item.objects.all()
#         extra_context = {'batch_list':batches,'employee_list': employees, 'item_list':items}
#         print extra_context
#         return super(BatchAdmin, self).changelist_view(request,extra_context=extra_context)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['date', 'employee','amount']
    search_fields = ['date', 'employee','amount']

class LoanAdmin(admin.ModelAdmin):
    list_display = ['date', 'employee','amount']
    search_fields = ['date', 'employee','amount']

def my_view(request, *args, **kwargs):
    return HttpsResponse(" <a href='/admin'>here to do nothing</a>")
admin.site.register(Item)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Batch)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Loan,LoanAdmin)
admin.site.register(CompanyDowntime)
admin.site.register(AttendanceException)
#remove unneeded items 
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
