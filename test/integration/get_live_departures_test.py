from unittest import TestCase
from src import get_live_departures

class LiveDeparturesIntegrationTest(TestCase):
    def check_live_departure_times_can_be_parsed_for_default_station(self):
        get_live_departures.train_departures_from_station()