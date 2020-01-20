from django.db import models
from django.utils.translation import ugettext_lazy as _

from goods import models as goods_models


class Carousel(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    desc = models.TextField(_("Description"))
    good = models.ForeignKey(goods_models.Good, verbose_name=_("Good"), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('Date Added'))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('Editing Date'))

    def __str__(self):
        return f'{self.good.name}: {self.title}'
    
    class Meta:
        verbose_name = _('good in carousel')
        verbose_name_plural = _('goods in carousel')
