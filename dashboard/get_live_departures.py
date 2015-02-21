import urllib2
from datetime import datetime, timedelta
from xml.etree import ElementTree

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard.settings")

from models import TrainDeparture


def train_departures_from_station(html=None, station="eai"):
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
        eta_query = base_query + '[-2:-1]'

        if eval(eta_query) == []:
            break
        elif eval(base_query) == []:
            break
        train = TrainDeparture(
            eta=(datetime.now() + timedelta(minutes=int(eval(eta_query + '[0]')))).strftime('%Y-%m-%d %H:%M:%S'),
            destination=eval(base_query + '[0]').upper(),
            station=station
        )
        train.save()