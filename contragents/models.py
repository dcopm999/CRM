import logging
from django.db import models
from django.utils.translation import ugettext_lazy as _

from addresses import models as addresses_models

LOGGER = logging.getLogger(__name__)
    
class Contragent(models.Model):
    '''
    TODO: Gis points for contragent
    '''
    name = models.CharField(max_length=250, verbose_name=_("Contragent name"))
    address_ur = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("Legal address"))
    country = models.ForeignKey(addresses_models.Country, on_delete=models.CASCADE, blank=True, null=True,  verbose_name=_("Country"))
    city = models.ForeignKey(addresses_models.City, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("City"))
    region = models.ForeignKey(addresses_models.Region, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Region"))
    district = models.ForeignKey(addresses_models.District, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("District"))
    street = models.ForeignKey(addresses_models.Street, verbose_name=_("Street"), on_delete=models.CASCADE)
    house = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("House"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date"), editable=False)
    edited = models.DateTimeField(auto_now=True, verbose_name=_("Edited date"), editable=False)
    inn = models.CharField(max_length=20, blank=True, verbose_name="ИНН")
    okonh = models.CharField(max_length=20, blank=True, verbose_name="ОКОНХ")
    okpo = models.CharField(max_length=20, blank=True, verbose_name="OKПO")
    oked = models.CharField(max_length=20, blank=True, verbose_name="OКЭД")
    code_nds = models.CharField(max_length=20, blank=True, verbose_name="РКП НДС")
    # point = models.PointField(blank=True, null=True, verbose_name=_("Gis point")
    
    class Meta:
        verbose_name_plural = _("Contragents")
        verbose_name = _("Contragent")
        ordering = ['name']

    def __str__(self):
        return self.name

class Contact(models.Model):
    contragent = models.ForeignKey(Contragent, on_delete=models.CASCADE, editable=False, verbose_name=_("Contragent"))
    first_name = models.CharField(max_length=50, verbose_name=_("First name"))
    middle_name = models.CharField(max_length=50, verbose_name=_("Middle name"))
    last_name = models.CharField(max_length=50, verbose_name=_("Last name"))
    phone = models.CharField(max_length=200, verbose_name=_("Phone number"), null=True, blank=True)
    position = models.CharField(max_length=50, verbose_name=_("Position"))
    role = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Role"))
    birthday = models.DateField(blank=True, null=True, verbose_name=_("Birth day"))
    created = models.DateTimeField(auto_now_add=True, editable=False,  verbose_name=_("Created"))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_("Edited"))
    
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")