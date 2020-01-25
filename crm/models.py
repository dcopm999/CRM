from django.db import models
from django.utils.translation import ugettext_lazy as _

from uuid import uuid4

from contragents.models import Contact, Contragent
from goods.models import Good


class TaskStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Task status'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date"), editable=False)
    edited = models.DateTimeField(auto_now=True, verbose_name=_("Edited date"), editable=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Task status')
        verbose_name_plural = _('Task statuses')


class Agreement(models.Model):
    RESULT = [
        (1, _('Accepted')),
        (2, _('Refused')),
        (3, _('In progress'))
    ]
    code = models.UUIDField(default=uuid4, editable=False, verbose_name=_('Unique agreement code'))
    contragent = models.ForeignKey(Contragent, verbose_name=_("Contragent"), on_delete=models.CASCADE)
    result = models.PositiveSmallIntegerField(choices=RESULT, default=3, verbose_name=_('Agreement result'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date"), editable=False)
    edited = models.DateTimeField(auto_now=True, verbose_name=_("Edited date"), editable=False)
    
    def __str__(self):
        return f'{self.code}: {self.result}'
    
    class Meta:
        verbose_name = _('Agreement')
        verbose_name_plural = _('Agreements')
    

class AgreementTask(models.Model):
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE, verbose_name=_('Agreement status'))
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE, verbose_name=_('Agreement'))
    # contact = models.ForeignKey(Contragent, verbose_name=_("Contact"), on_delete=models.CASCADE)
    desc = models.TextField(verbose_name=_('Description'))
    date = models.DateTimeField(auto_now=True, verbose_name=_('Task date'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date"), editable=False)
    edited = models.DateTimeField(auto_now=True, verbose_name=_("Edited date"), editable=False)

    def __str__(self):
        return f'{self.agreement}'

    def contragent(self):
        return self.agreement.contragent
    
    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

class AgreementItem(models.Model):
    agreement = models.ForeignKey(Agreement, verbose_name=_("Agreement"), on_delete=models.CASCADE)
    good = models.ForeignKey(Good, verbose_name=_("Good"), on_delete=models.CASCADE)
    count = models.PositiveIntegerField(_("Count"))

    def __str__(self):
        return f'{self.good}: {self.count}'
    
    class Meta:
        verbose_name = _('Agreement item')
        verbose_name_plural = _('Agreement items')
    
