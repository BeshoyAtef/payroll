from django.contrib import admin

def my_view(request, *args, **kwargs):
    return HttpResponse(" <a href='/admin'>here to do nothing</a>")

# admin.site.register_view('somepath', my_view, 'My Fancy Admin View!')

# And of course, this still works:
from www.models import *

admin.site.register(Employee)
admin.site.register(AttendanceException)
admin.site.register(CompanyDowntime)
# admin.site.register(Item)
admin.site.register(Batch)
admin.site.register(Payment)
admin.site.register(Loan)

from django.contrib import admin
from django.shortcuts import redirect

from admin_views.admin import AdminViews


class TestAdmin(AdminViews):
    admin_views = (
                    ('Redirect to CNN test', 'redirect_to_cnn'),
                    ('Test Method', 'http://www.revsys.com'),
        )

    def redirect_to_cnn(self, *args, **kwargs):
        return redirect('http://www.cnn.com')

admin.site.register(Item, TestAdmin)
