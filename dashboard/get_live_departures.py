import urllib2
from xml.etree import ElementTree

from dashboard.time_formatting import datetime_plus


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

        if eval('all_elements[%s].%s.strip()' % (e[0], e[1])) == '':
            continue

        base_query = 'all_elements[%s].%s.strip()[2:].split()' % (e[0], e[1])
        eta_query = base_query + '[-2:-1]'

        eta = None

        if eval(base_query) is []:
            continue

        if eval(eta_query) is not []:
            try:
                eta = (datetime_plus(minutes=int(eval(eta_query + '[0]')))).strftime('%Y-%m-%d %H:%M:%S')
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

    return trains