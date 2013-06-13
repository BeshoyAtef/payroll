from django.contrib import admin
from www.views import import_attendance
from django.http import HttpResponse


def my_view(request, *args, **kwargs):
    return HttpsResponse(" <a href='/admin'>here to do nothing</a>")


# And of course, this still works:
from www.models import *

admin.site.register(Employee)

# admin.site.register(Item)
admin.site.register(Batch)


from django.shortcuts import redirect

from admin_views.admin import AdminViews

class TestAdmin(AdminViews):
    admin_views = (
                    ('Test Report', 'redirect_to_cnn'),
                    ('Upload Attendance-Log','import_attendance'),
        )

    def redirect_to_cnn(self, *args, **kwargs):
        return HttpResponse(" <a href='/admin'>here to do nothing</a>")

admin.site.register(Item, TestAdmin)
