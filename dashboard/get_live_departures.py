import urllib2
from datetime import datetime, timedelta
from xml.etree import ElementTree

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard.settings")

# from models import TrainDeparture


def train_departures_from_station(html=None, station="eai"):
    # TrainDeparture.objects.filter(station=station).delete()

    html = html or urllib2.urlopen("http://www.dlrlondon.co.uk/xml/mobile/%s.xml" % station).read()
    xml_file = ElementTree.fromstring(html)
    all_elements = xml_file.findall(".//")
    element_list = [
        (4, 'text'),
        (7, 'text'),
        (8, 'tail'),
        (16, 'text'),
        (19, 'text'),
        (20, 'tail')
    ]

    for e in element_list:

        base_query = 'all_elements[%s].%s.strip()[2:].split()' % (e[0], e[1])

        if eval(base_query[-2:-1]) == []:
            break
        elif eval(base_query) == []:
            break
        else:
            eta=(datetime.now() + timedelta(minutes=eval("base_query[-2:-1][0]" % (e[0], e[1])))).strftime('%Y-%m-%d %H:%M:%S'),
            destination=eval("base_query[0]" % (e[0], e[1])).upper(),
            station=station

            # train.save()


train_departures_from_station()