'''
package: stocks
description: models
'''
from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _

from contragents.models import Contragent
from addresses import models as addresses_models
from pricing import models as pricing_models
from goods import models as good_models


class Stock(models.Model):
    '''
    Model for stocks
    '''
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    country = models.ForeignKey(addresses_models.Country, on_delete=models.CASCADE, verbose_name=_("Country"))
    region = models.ForeignKey(addresses_models.Region, on_delete=models.CASCADE, verbose_name=_("Region"))
    city = models.ForeignKey(addresses_models.City, on_delete=models.CASCADE, verbose_name=_("City"))
    district = models.ForeignKey(addresses_models.District, on_delete=models.CASCADE, verbose_name=_("District"))
    street = models.ForeignKey(addresses_models.Street, verbose_name=_("Street"), on_delete=models.CASCADE)
    house = models.CharField(max_length=50, verbose_name=_("House"))
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('date of creation'))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('date of edition'))


    def total_amount_base(self):
        '''
        counting total base price of all lots in particular stock
        :return:
        TODO: Сделать агрегативную функцию 
        '''
        summ = Decimal()
        for lot in self.lot_set.all():
            summ += lot.total_amount()
        return summ

    def __str__(self):
        '''
        str method for Stock model
        :return:
        '''
        return self.name

    class Meta:
        '''
        meta class for stock
        '''
        verbose_name = _('Stock')
        verbose_name_plural = _('Stocks')


class Lot(models.Model):
    '''

   Model for lots
    '''
    series = models.CharField(max_length=20, verbose_name=_('series'))
    good = models.ForeignKey(good_models.Good, on_delete=models.CASCADE, verbose_name=_('Good'))
    base_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_('Base price'))
    currency = models.ForeignKey(pricing_models.Currency, on_delete=models.CASCADE, verbose_name=_('Currency'))
    shelf_life = models.DateField(verbose_name=_('shelf life'))
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('date of creation'))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('date of edition'))
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, verbose_name=_('Stock'))

    def total_amount(self):
        return self.base_price * self.quantity

    def __str__(self):
        '''
        overlapped str method for Lot model
        :return:
        '''
        return self.series

    class Meta:
        '''
        meta class for lots
        '''
        verbose_name = _('Lot')
        verbose_name_plural = _('Lots')
