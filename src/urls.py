from django.conf.urls import patterns, include, url
from django.contrib import admin
from src.views import IndexView

urlpatterns = patterns('',
    # Examples:
    url('^.*$', IndexView.as_view(), name='index'),
    # url(r'^$', 'dash.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
