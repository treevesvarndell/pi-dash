from unittest import TestCase
from src import get_live_departures

class LiveDeparturesIntegrationTest(TestCase):
    def get_live_departures_integration_test(self):
        get_live_departures.train_departures_from_station()