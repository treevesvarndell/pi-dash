import urllib2
from pprint import pprint
from datetime import datetime, timedelta
from xml.etree import ElementTree


def train_departures_from_station(html=None, station="eai"):
    html = html or urllib2.urlopen("http://www.dlrlondon.co.uk/xml/mobile/%s.xml" % station).read()
    xml_file = ElementTree.fromstring(html)
    all_elements = xml_file.findall(".//")
    element_list = [
        (4, 'text', 'east'),
        (7, 'text', 'east'),
        (8, 'tail', 'east'),
        (16, 'text', 'west'),
        (19, 'text', 'west'),
        (20, 'tail', 'west')
    ]

    trains = []

    for e in element_list:
        base_query = 'all_elements[%s].%s.strip()[2:].split()' % (e[0], e[1])
        eta_query = base_query + '[-2:-1]'

        eta = None

        if eval(base_query) == []:
            break

        if eval(eta_query) != []:
            try:
                eta = (datetime.now() + timedelta(minutes=int(eval(eta_query + '[0]')))).strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                eta = None

        destination = eval(base_query)

        if len(destination) > 2:
            destination.pop()
            destination.pop()

        trains.append({
            'direction': (e[2]),
            'eta': eta,
            'destination': ' '.join(destination).upper(),
            'station': station
        })

    pprint(trains)
    return trains


train_departures_from_station()