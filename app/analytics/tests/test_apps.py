from django.test import TestCase

from analytics.apps import AnalyticsConfig


class AnalyticsConfigAppTests(TestCase):

    def test_app_name(self):
        self.assertEqual(AnalyticsConfig.name, "analytics")
