from unittest import TestCase
from src import get_live_departures

class LiveDeparturesUnitTest(TestCase):
    def test_get_live_departures(self):
        actual = get_live_departures.train_departures_from_station(html=test_html)
        expected = {
            "timestamp": "23:01",
            "east1": "1 Woolwich Arsn   2 mins",
            "east2": "2 BECKTON         9 MINS",
            "east3": "3 WOOLWICH ARSN  12 MINS",
            "west1": "1 Bank            4 mins",
            "west2": "2 TOWER GATEWAY   8 MINS",
            "west3": "3 BANK           14 MINS"
        }
        self.assertDictEqual(actual, expected)


test_html = '''<?xml version="1.0" encoding="UTF-8"?>
<ttBoxset xmlns="http://www.dlrmobile.org/schemas/sitemap/0.9">
  <div id="ttbox">
    <div id="platformleft">
      <img src="p1l.gif" alt="" width="54" height="86" border="0" />
    </div>
    <div id="platformmiddle">
      <div id="line1">
1 Woolwich Arsn   2 mins
				</div>
      <div id="clearall">
      </div>
      <div id="line23">
        <p>
2 BECKTON         9 MINS

<br />

3 WOOLWICH ARSN  12 MINS
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
1 Bank            4 mins
				</div>
      <div id="clearall">
      </div>
      <div id="line23">
        <p>
2 TOWER GATEWAY   8 MINS

<br />

3 BANK           14 MINS
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