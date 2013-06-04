from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from beta.urls import *
from payments.urls import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'condomsxl.views.home', name='home'),
    # url(r'^condomsxl/', include('condomsxl.foo.urls')),
	url(r'^payments/', include('payments.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
)
