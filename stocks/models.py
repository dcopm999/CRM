'''
package: stocks
description: models
'''
from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _
from contragents.models import Contragent
from addresses import models as addresses_models


class Stock(models.Model):
    '''
    Model for stocks
    '''
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    country = models.ForeignKey(addresses_models.Country, on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name=_("Country"))
    city = models.ForeignKey(addresses_models.City, on_delete=models.CASCADE, blank=True, null=True,
                             verbose_name=_("City"))
    region = models.ForeignKey(addresses_models.Region, on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name=_("Region"))
    district = models.ForeignKey(addresses_models.District, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name=_("District"))
    street = models.ForeignKey(addresses_models.Street, verbose_name=_("Street"), on_delete=models.CASCADE)
    house = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("House"))
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('date of creation'))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('date of edition'))


    def total_amount_base(self):
        '''
        counting total base price of all lots in particular stock
        :return:
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

    class Meta:   #pylint: disable=too-few-public-methods
        '''
        meta class for stock
        '''
        verbose_name = _('Stock')
        verbose_name_plural = _('Stocks')
