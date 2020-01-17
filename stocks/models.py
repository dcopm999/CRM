'''
package: stocks
description: models
'''
from uuid import uuid4
from django.db import models
from contragents.models import Contragent
from goods.models import Good

class Stock(models.Model):
    '''
    Model for stocks
    '''
    name = models.CharField(max_length=100, verbose_name='Название')
    contragent = models.ForeignKey(Contragent, on_delete=models.CASCADE, verbose_name='Контрагент')
    address = models.TextField(max_length=500, verbose_name='Адрес')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(auto_now=True, editable=False)

    def total_amount(self):
        return self.lot_set.aggregate(models.Sum('total_price')).get('total_price__sum')

    def save(self, *args, **kwargs):
        self.code = f'{self.contragent.name}'

    def __str__(self):
        '''
        str method for Stock model
        :return:
        '''
        return f'{self.name}'

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'


class Lot(models.Model):
    '''
    Model for lots
    '''
    CURRENCY = (
        ('sum', 'UZS'),
        ('usd', 'USD'),
        ('rub', 'RUB'),
    )
    lot_number = models.CharField(max_length=50, blank=True, editable=False, verbose_name='Номер партии')
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='Товар')
    base_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Базовая цена')
    selling_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Продажная цена')
    series = models.CharField(max_length=20, verbose_name='Серия')
    currency = models.CharField(max_length=20, choices=CURRENCY, default='UZS', verbose_name='Валюта')
    total_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, editable=False, verbose_name='Общая цена')
    shelf_life = models.DateField(verbose_name='Срок годности')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(auto_now=True, editable=False)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, verbose_name='Склад')

    def save(self, *args, **kwargs):
        '''
        overlapped save method for Lot method
        :param args:
        :param kwargs:
        :return:
        '''
        self.lot_number = f'Партия {str(uuid4())[:8]}'
        self.total_price = self.price * self.quantity
        super(Lot, self).save(*args, **kwargs)

    def __str__(self):
        '''
        overlapped str method for Lot model
        :return:
        '''
        return f'{self.lot_number}'

    class Meta:
        verbose_name = 'Партию'
        verbose_name_plural = 'Партия'

