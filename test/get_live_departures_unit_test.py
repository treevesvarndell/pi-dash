import unittest
from datetime import datetime, timedelta
import random

from mock import patch

from dashboard.get_live_departures import train_departures_from_station


class LiveDeparturesUnitTest(unittest.TestCase):
    def setUp(self):
        year = random.randint(1950, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)

        self.mock_time = datetime(year, month, day)
        self.patch_time = patch('dashboard.time_formatting.datetime_now', return_value=self.mock_time)
        self.patch_time.start()

    def tearDown(self):
        self.patch_time.stop()

    def get_time_plus_minutes(self, minutes):
        return (self.mock_time + timedelta(minutes=minutes)).strftime("%Y-%m-%d %H:%M:%S")

    def test_departure_times_are_returned(self):
        html = test_html.format(
            time1="1 Woolwich Arsn   2 mins",
            time2="2 BECKTON         9 MINS",
            time3="3 BECKTON         9 MINS",
            time4="1 Bank            4 mins",
            time5="2 TOWER GATEWAY   8 MINS",
            time6="3 BANK           14 MINS"
        )
        actual = train_departures_from_station(html=html)
        expected = [
            {"destination": "WOOLWICH ARSN", "direction": "east", "station": "eai",
             "eta": self.get_time_plus_minutes(2)},
            {"destination": "BECKTON", "direction": "east", "station": "eai", "eta": self.get_time_plus_minutes(9)},
            {"destination": "BECKTON", "direction": "east", "station": "eai", "eta": self.get_time_plus_minutes(9)},
            {"destination": "BANK", "direction": "west", "station": "eai", "eta": self.get_time_plus_minutes(4)},
            {"destination": "TOWER GATEWAY", "direction": "west", "station": "eai",
             "eta": self.get_time_plus_minutes(8)},
            {"destination": "BANK", "direction": "west", "station": "eai", "eta": self.get_time_plus_minutes(14)}
        ]

        for x in xrange(0, len(expected)):
            self.assertDictEqual(actual[x], expected[x])

    def test_departure_time_set_to_null_if_departure_time_not_present(self):
        html = test_html.format(
            time1="1 Woolwich Arsn",
            time2="2 BECKTON         9 MINS",
            time3="3 BECKTON         9 MINS",
            time4="1 Bank            4 mins",
            time5="2 TOWER GATEWAY   8 MINS",
            time6="3 BANK           14 MINS"
        )
        actual = train_departures_from_station(html=html)
        expected = [
            {"destination": "WOOLWICH ARSN", "direction": "east", "station": "eai", "eta": None}
        ]

        self.assertDictContainsSubset(actual[0], expected[0])

    def test_handle_only_two_trains_displayed(self):
        html = test_html.format(
            time1="1 Woolwich Arsn",
            time2="",
            time3="",
            time4="1 Bank            4 mins",
            time5="2 TOWER GATEWAY   8 MINS",
            time6=""
        )
        actual = train_departures_from_station(html=html)
        expected = [
            {"destination": "WOOLWICH ARSN", "direction": "east", "station": "eai", "eta": None},
            {"destination": "BANK", "direction": "west", "station": "eai", "eta": self.get_time_plus_minutes(4)},
            {"destination": "TOWER GATEWAY", "direction": "west", "station": "eai",
             "eta": self.get_time_plus_minutes(8)}
        ]

        for x in xrange(0, len(expected)):
            self.assertDictContainsSubset(actual[x], expected[x])


test_html = '''<?xml version="1.0" encoding="UTF-8"?>
<ttBoxset xmlns="http://www.dlrmobile.org/schemas/sitemap/0.9">
  <div id="ttbox">
    <div id="platformleft">
      <img src="p1l.gif" alt="" width="54" height="86" border="0" />
    </div>
    <div id="platformmiddle">
      <div id="line1">
{time1}
				</div>
      <div id="clearall">
      </div>
      <div id="line23">
        <p>
{time2}

<br />

{time3}
				</p>
      </div>
      <div id="time">
23:01
				</div>
    </div>
    <div id="platformright">
      <img src="p1r.gif" alt="" width="57" height="86" border="0" />
    </div>
  </div>
  <div id="ttbox">
    <div id="platformleft">
      <img src="p2l.gif" alt="" width="54" height="86" border="0" />
    </div>
    <div id="platformmiddle">
      <div id="line1">
{time4}
				</div>
      <div id="clearall">
      </div>
      <div id="line23">
        <p>
{time5}

<br />

{time6}
				</p>
      </div>
      <div id="time">
23:01

			</div>
    </div>
    <div id="platformright">
      <img src="p2r.gif" alt="" width="57" height="86" border="0" />
    </div>
  </div>
</ttBoxset>'''