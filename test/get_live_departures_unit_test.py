import unittest

from get_live_departures import train_departures_from_station


class LiveDeparturesUnitTest(unittest.TestCase):
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
            {"destination": "WOOLWICH ARSN", "direction": "east", "station": "eai"},
            {"destination": "BECKTON", "direction": "east", "station": "eai"},
            {"destination": "BECKTON", "direction": "east", "station": "eai"},
            {"destination": "BANK", "direction": "west", "station": "eai"},
            {"destination": "TOWER GATEWAY", "direction": "west", "station": "eai"},
            {"destination": "BANK", "direction": "west", "station": "eai"}
        ]

        for x in xrange(0, len(expected)):
            actual[0].pop("eta", None)
            self.assertDictEqual(actual[0], expected[0])

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
        expected = [{
                        "destination": "WOOLWICH ARSN", "direction": "east", "station": "eai", "eta": None
                    }]

        self.assertDictEqual(actual[0], expected[0])


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