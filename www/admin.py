from django.contrib import admin
from www.views import import_attendance
from django.http import HttpResponse
from www.models import *
from django.shortcuts import redirect
from admin_views.admin import AdminViews

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','mobile', 'ssn']
    search_fields = ['name', 'email','mobile', 'ssn']

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
