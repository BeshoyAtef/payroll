from django.contrib import admin
from www.models import *

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','mobile', 'ssn']
    search_fields = ['name', 'email','mobile', 'ssn']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Batch)
admin.site.register(Payment)
admin.site.register(Loan)
admin.site.register(CompanyDowntime)
admin.site.register(Item)


