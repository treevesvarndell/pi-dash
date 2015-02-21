from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from dashboard.models import TrainDeparture
from dashboard.views import IndexView
from get_live_departures import train_departures_from_station

admin.site.register(TrainDeparture)

class TrainDepartureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainDeparture
        fields = ('created_at', 'eta', 'destination', 'station')

class TrainDepartureViewSet(viewsets.ReadOnlyModelViewSet):
    train_departures_from_station()
    queryset = TrainDeparture.objects.all()
    serializer_class = TrainDepartureSerializer()

    def list(self, request):
        TrainDeparture.objects.all().delete()
        train_departures_from_station()
        serializer = TrainDepartureSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'departures', TrainDepartureViewSet)

urlpatterns = patterns('',
                       # Examples:
                       url('^/?$', IndexView.as_view(), name='index'),
                       url(r'^api/', include(router.urls, namespace='api')),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/?', include(admin.site.urls)),
)
