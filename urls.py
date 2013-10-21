from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'silky.views.home', name='home'),
    # url(r'^silky/', include('silky.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'views.home', name='home'),
     url(r'^admin/', include(admin.site.urls)),
    url(r'^enquiry/$','enquiry.views.enquiry', name='enquiry'),
)
