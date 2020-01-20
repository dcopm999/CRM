from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Country"))
    
    class Meta:
        verbose_name_plural = _("Countries")
        verbose_name = _("Country code")
        
    def __str__(self):
        return self.name


class Region(models.Model):
    parent = models.ForeignKey(Country, verbose_name=_("Country"), on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Region"))

    class Meta:
        verbose_name_plural = _("Regions")
        verbose_name = _("Region")

    def __str__(self):
        return self.name


class City(models.Model):
    parent = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=_("Region"))
    name = models.CharField(max_length=100, unique=True, verbose_name=_("City"))

    class Meta:
        verbose_name_plural = _("Cities")
        verbose_name = _("City")

    def __str__(self):
        return self.name


class District(models.Model):
    parent = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True, verbose_name=_("District"))

    class Meta:
        verbose_name_plural = _("Districts")
        verbose_name = _("District")

    def __str__(self):
        return self.name


class Street(models.Model):
    parent = models.ForeignKey(District, verbose_name=_("District"), on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("Street"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = _("Streets")
        verbose_name = _("Street")
