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

    url(r'^read$', 'www.views.upload_file'),


    url(r'^view/$', 'www.views.view_page', name='home'),
    url(r'^view/test/$', 'www.views.dummy_method', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_batch/', 'www.views.add_batch')

)


