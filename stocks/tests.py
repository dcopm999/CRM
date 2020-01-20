from decimal import Decimal
from django.test import TestCase
from . import models

class StocksModelsTestCase(TestCase):

    fixtures = ['fixture_stock.json']

    def setUp(self) -> None:
        self.stock = models.Stock.objects.last()

    def test_stock_str(self):
        self.assertEqual(self.stock.__str__(), 'Склад 1')

    def test_stock_total_amount_base(self):
        self.assertEqual(self.stock.total_amount_base(), Decimal('25.00'))

