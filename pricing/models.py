from django.db import models
from django.utils.translation import ugettext_lazy as _

class Pricing(models.Model):
    '''
    model for pricing models
    '''
    name = models.CharField(max_length=200, verbose_name=_('pricing model name'))
    coefficient = models.FloatField(verbose_name=_('coefficient'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Pricing model')
        verbose_name_plural = _('Pricing models')


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

    class Meta:
        '''
        meta class for currency
        '''
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')
