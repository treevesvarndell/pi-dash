from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import IndexView, ScreenView


urlpatterns = patterns('',
                       # Examples:
                       url(r'^api/screen/?', ScreenView.as_view(), name='screen'),
                       url('^/?$', IndexView.as_view(), name='index'),
                       url(r'^admin/?', include(admin.site.urls)),
)
