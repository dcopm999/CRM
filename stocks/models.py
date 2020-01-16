'''
package: stocks
description: models
'''
from uuid import uuid4
from django.db import models

#from goods.models import Good

class Stock(models.Model):
    '''
    Model for stocks
    '''
    name = models.CharField(max_length=100, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
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
    #good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='Товар')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена')
    currency = models.CharField(max_length=20, choices=CURRENCY, default='UZS', verbose_name='Валюта')
    total_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, editable=False, verbose_name='Общая цена')
    shelf_life = models.DateField(verbose_name='Срок годности')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(auto_now=True, editable=False)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, verbose_name='Склад')

    def save(self, *args, **kwargs):
        self.lot_number = f'Партия {str(uuid4())[:8]}'
        self.total_price = self.price * self.quantity
        super(Lot, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.lot_number}'

    class Meta:
        verbose_name = 'Партию'
        verbose_name_plural = 'Партия'

