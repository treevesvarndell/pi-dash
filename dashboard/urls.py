from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import IndexView, ScreenApiView, ScreenView


urlpatterns = patterns('',
                       # Examples:
                       url(r'^screen/?', ScreenView.as_view(), name='screen toggle'),
                       url(r'^api/screen/?', ScreenApiView.as_view(), name='screen api'),
                       url('^/?$', IndexView.as_view(), name='index'),
                       url(r'^admin/?', include(admin.site.urls)),
)
