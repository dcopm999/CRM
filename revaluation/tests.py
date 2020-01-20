from django.test import TestCase
from . import models

class PricingModelTestCase(TestCase):

    fixtures = ['fixture_reval.json']

    def setUp(self):
        self.pricing = models.Pricing.objects.last()

    def test_pricing_str(self):
        self.assertEqual(self.pricing.__str__(), 'обычная')