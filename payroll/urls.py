from django.conf.urls import patterns, include, url
from www.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# from adminplus.sites import AdminSitePlus

# admin.site = AdminSitePlus()
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'www.views.index', name='home'),
    # url(r'^payroll/', include('payroll.foo.urls')),
    url(r'^view/$', 'www.views.view_page', name='home'),
    url(r'^view/test/$', 'www.views.dummy_method', name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^employeeReport/$', 'www.views.view_report_page'),
    url(r'^hours_month/$', 'www.views.employee_workinghours_month'),
    url(r'^hours_year/$', 'www.views.employee_workinghours_year'),
    # url(r'^products_month/$', 'www.views.employee_workinghours_year'),
    # url(r'^products_year/$', 'www.views.employee_workinghours_year'),
    url(r'^productivity_month/$', 'www.views.employee_productivity_month'),
    url(r'^productivity_year/$', 'www.views.employee_productivity_year'),
    url(r'^payement_month/$', 'www.views.employee_payement_month'),
    url(r'^payement_year/$', 'www.views.employee_payement_year'),
    url(r'^attendance_month/$', 'www.views.employee_workinghours_year'),
    url(r'^attendance_year/$', 'www.views.employee_workinghours_year')
)