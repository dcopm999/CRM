from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class StocksConfig(AppConfig):
    name = 'stocks'
    verbose_name = _('Stocks')

