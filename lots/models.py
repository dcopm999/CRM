'''
package: lots
description: models
'''
from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext_lazy as _
from stocks.models import Stock
from goods.models import Good


class Currency(models.Model):
    '''
    model for currencies
    '''
    name = models.CharField(max_length=50, verbose_name=_('Currency'))

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
        verbose_name = _('currency')
        verbose_name_plural = _('currencies')


class Lot(models.Model):
    '''
    Model for lots
    '''
    lot_number = models.CharField(max_length=50,
                                  blank=True,
                                  editable=False,
                                  verbose_name=_('lot number'))
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name=_('Product'))
    base_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_('base price'))
    series = models.CharField(max_length=20, verbose_name=_('series'))
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name=_('currency'))
    shelf_life = models.DateField(verbose_name=_('shelf life'))
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('date of creation'))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('date of edition'))
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, verbose_name=_('Stock'))

    def save(self, *args, **kwargs):  #pylint: disable=arguments-differ
        '''
        overlapped save method for Lot method
        :param args:
        :param kwargs:
        :return:
        '''
        self.lot_number = f'Партия {str(uuid4())[:8]}'
        super(Lot, self).save(*args, **kwargs)

    def total_amount(self):
        return self.base_price * self.quantity

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
        verbose_name = _('Lot')
        verbose_name_plural = _('Lots')
