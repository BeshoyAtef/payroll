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
    url(r'^view_output_yearly/$', 'www.views.view_output_yearly', name='home'),
    url(r'^view_output_monthly/$', 'www.views.view_output_monthly', name='home'),
    url(r'^goToCompanyReports$', 'www.views.goToCompanyReports'),
    url(r'^getSalary/$', 'www.views.company_wide_salaryReport'),
    url(r'^getOutputYearly/$', 'www.views.company_wide_output_yearlyReport'),
    url(r'^getAttendanceYearly/$', 'www.views.company_wide_yearly_attendanceReport'),
    url(r'^getOutputMonthly/$', 'www.views.company_wide_output_monthlyReport'),
    url(r'^getAttendanceMonthly/$', 'www.views.company_wide_monthly_attendanceReport'),
    # url(r'^payroll/', include('payroll.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)