"""
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agroeco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

)
"""
from django.conf.urls import include, url
from oscar.app import application

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
  url(r'^admin/', include(admin.site.urls)),
  url(r'^i18n/', include('django.conf.urls.i18n')),
  url(r'', include(application.urls))
  ]
