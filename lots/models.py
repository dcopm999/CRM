'''
package: lots
description: models
'''
from uuid import uuid4
from django.db import models
from stocks.models import Stock
from goods.models import Good


class Currency(models.Model):
    '''
    model for currencies
    '''
    name = models.CharField(max_length=50, verbose_name='Валюта')

    def __str__(self):
        '''
        overlapping str method for currency
        :return:
        '''
        return self.name

    class Meta:  #pylint: disable=too-few-public-methods
        '''
        meta class for currency
        '''
        verbose_name = 'Валюту'
        verbose_name_plural = 'Валюта'


class Lot(models.Model):
    '''
    Model for lots
    '''
    lot_number = models.CharField(max_length=50,
                                  blank=True,
                                  editable=False,
                                  verbose_name='Номер партии')
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='Товар')
    base_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Базовая цена')
    selling_price = models.DecimalField(max_digits=20,
                                        decimal_places=2,
                                        verbose_name='Цена на продажу')
    series = models.CharField(max_length=20, verbose_name='Серия')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name='Валюта')
    total_base_price = models.DecimalField(max_digits=20,
                                           decimal_places=2,
                                           blank=True,
                                           editable=False,
                                           verbose_name='Общая базовая цена')
    total_selling_price = models.DecimalField(max_digits=20,
                                              decimal_places=2,
                                              blank=True,
                                              editable=False,
                                              verbose_name='Общая цена на продажу')
    shelf_life = models.DateField(verbose_name='Срок годности')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(auto_now=True, editable=False)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, verbose_name='Склад')

    def save(self, *args, **kwargs):  #pylint: disable=arguments-differ
        '''
        overlapped save method for Lot method
        :param args:
        :param kwargs:
        :return:
        '''
        self.lot_number = f'Партия {str(uuid4())[:8]}'
        self.total_base_price = self.base_price*self.quantity
        self.total_selling_price = self.selling_price*self.quantity
        super(Lot, self).save(*args, **kwargs)

    def __str__(self):
        '''
        overlapped str method for Lot model
        :return:
        '''
        return self.lot_number

    class Meta:  #pylint: disable=too-few-public-methods
        '''
        meta class for lots
        '''
        verbose_name = 'Партию'
        verbose_name_plural = 'Партия'
