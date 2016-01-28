from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import IndexView


urlpatterns = patterns('',
                       # Examples:
                       url('^/?$', IndexView.as_view(), name='index'),
                       url(r'^admin/?', include(admin.site.urls)),
)
