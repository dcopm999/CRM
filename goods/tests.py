"""
Goods.tests
"""
from django.test import TestCase

from . import models


class GoodsTestCase(TestCase):
    '''
    Tests for goods application
    '''
    fixtures = ['fixture_goods.json']

    def setUp(self):
        '''
        method for defining required data
        '''
        self.trade_name = models.TradeName.objects.last()
        self.maker = models.Maker.objects.last()
        self.category = models.Category.objects.last()
        self.measure = models.Measure.objects.last()
        self.packing = models.Packing.objects.last()
        self.original = models.Original.objects.last()
        self.good = models.Good.objects.last()

    def test_trade_mame_str(self):
        '''
        test for TradeName model's __str__ method
        '''
        self.assertEqual(self.trade_name.__str__(), 'Молоко')

    def test_maker_str(self):
        '''
        test for Maker model's __str__ method
        '''
        self.assertEqual(self.maker.__str__(), 'Nestle, Узбекистан')

    def test_category_str(self):
        '''
        test for Category model's __str__ method
        '''
        self.assertEqual(self.category.__str__(), 'Продукты питания')

    def test_measure_str(self):
        '''
        test for Measure model's __str__ method
        '''
        self.assertEqual(self.measure.__str__(), 'литр')

    def test_packing_str(self):
        '''
        test for Packing model's __str__ method
        '''
        self.assertEqual(self.packing.__str__(), 'TetraPak')

    def test_original_str(self):
        '''
        test for Original model's __str__ method
        '''
        self.assertEqual(self.original.__str__(), '12')

    def test_good_str(self):
        '''
        test for Good model's __str__ method
        '''
        self.assertEqual(self.good.__str__(), 'Молоко, Nestle, Узбекистан, Продукты питания')

    def test_good_save(self):
        '''
        test for Good model's save method
        '''
        self.assertEqual(self.good.slug, 'moloko-nestle-uzbekistan')
