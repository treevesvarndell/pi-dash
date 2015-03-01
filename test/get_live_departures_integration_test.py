import unittest

from dashboard.get_live_departures import train_departures_from_station


class LiveDeparturesIntegrationTest(unittest.TestCase):
    def test_live_departure_times_can_be_parsed_for_default_station(self):
        actual = train_departures_from_station()

        expected_keys = ["destination", "direction", "eta", "station"]

        for value in actual:
            self.assertListEqual(value.keys(), expected_keys)
