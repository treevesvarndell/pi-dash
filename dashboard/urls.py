from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashboard.models import TrainDeparture
from dashboard.views import IndexView

admin.site.register(TrainDeparture)

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/?', include(admin.site.urls)),
    url('^.*$', IndexView.as_view(), name='index'),
    # url(r'^$', 'dash.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
)
