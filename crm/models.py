from django.db import models
from django.utils.translation import ugettext_lazy as _

from uuid import uuid4


class AgreementStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Agreement status'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date"), editable=False)
    edited = models.DateTimeField(auto_now=True, verbose_name=_("Edited date"), editable=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Agreement status')
        verbose_name_plural = _('Agreement statuses')


class Agreement(models.Model):
    RESULT = [
        (1, _('Accepted')),
        (2, _('Refused')),
        (3, _('In progress'))
    ]
    code = models.UUIDField(default=uuid4, verbose_name=_('Unique agreement code'))
    status = models.ForeignKey(AgreementStatus, on_delete=models.CASCADE, verbose_name=_('Agreement status'))
    result = models.PositiveSmallIntegerField(choices=RESULT, verbose_name=_('Agreement result'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date"), editable=False)
    edited = models.DateTimeField(auto_now=True, verbose_name=_("Edited date"), editable=False)
    
    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = _('Agreement')
        verbose_name_plural = _('Agreements')
    
