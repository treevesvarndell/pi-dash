from xml.etree import ElementTree
import urllib2


def get_live_departures(html=None, station="eai"):
    html = html or urllib2.urlopen("http://www.dlrlondon.co.uk/xml/mobile/%s.xml" % station).read()
    xml_file = ElementTree.fromstring(html)

    info = {
        "timestamp": xml_file.findall(".//")[9].text.strip(),
        "east1": xml_file.findall(".//")[4].text.strip(),
        "east2": xml_file.findall(".//")[7].text.strip(),
        "east3": xml_file.findall(".//")[8].tail.strip(),
        "west1": xml_file.findall(".//")[16].text.strip(),
        "west2": xml_file.findall(".//")[19].text.strip(),
        "west3": xml_file.findall(".//")[20].tail.strip()
    }

    return info


def main():
    get_live_departures()

