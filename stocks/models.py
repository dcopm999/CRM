'''
package: stocks
description: models
'''
from django.db import models
from contragents.models import Contragent


class Stock(models.Model):
    '''
    Model for stocks
    '''
    name = models.CharField(max_length=100, verbose_name='Название')
    contragent = models.ForeignKey(Contragent, on_delete=models.CASCADE, verbose_name='Контрагент')
    address = models.TextField(max_length=500, verbose_name='Адрес')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(auto_now=True, editable=False)

    def total_amount_base(self):
        '''
        counting total base price of all lots in particular stock
        :return:
        '''
        return self.lot_set.aggregate(models.Sum('total_base_price')).get('total_base_price__sum') #pylint: disable=no-member

    def total_amount_sell(self):
        '''
        counting total selling price of all lots in particular stock
        :return:
        '''
        return self.lot_set.aggregate(                                         #pylint: disable=no-member
            models.Sum('total_selling_price')).get('total_selling_price__sum')

    def __str__(self):
        '''
        str method for Stock model
        :return:
        '''
        return self.name

    class Meta:   #pylint: disable=too-few-public-methods
        '''
        meta class for stock
        '''
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'
