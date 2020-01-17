"""
Goods.app
"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GoodsConfig(AppConfig):
    """
    Application name
    """
    name = 'goods'
    verbose_name = _('Goods')
