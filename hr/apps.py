from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class HrConfig(AppConfig):
    name = 'hr'
    verbose_name = _('Human resource')
