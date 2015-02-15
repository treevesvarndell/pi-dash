from unittest import TestCase
from dash.dash import pull_data

class LiveDeparturesIntegrationTest(TestCase):
    def get_live_departures_integration_test(self):
        pull_data.get_live_departures()