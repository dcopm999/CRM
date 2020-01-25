"""
Goods.models
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from pytils.translit import slugify

from addresses.models import Country


class Maker(models.Model):
    """
    Model Maker for Good
    """
    name = models.CharField(max_length=250, unique=True, verbose_name=_('Name of manufacturer'))
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_('The country of manufacture'))
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('Date Added'))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('Editing Date'))

    def __str__(self):
        return f'{self.name}, {self.country}'

    class Meta:
        verbose_name = _('Manufacturer')
        verbose_name_plural = _('Manufacturers')


class TradeName(models.Model):
    """
    Model TradeName for Good
    """
    name = models.CharField(max_length=250, unique=True, verbose_name=_('Product Name'))
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('Date Added'))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('Editing Date'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product Name')
        verbose_name_plural = _('Product Names')


class Category(models.Model):
    """
    Model Category for Good
    """
    name = models.CharField(max_length=250, unique=True, verbose_name=_('Category Name'))
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('Date Added'))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('Editing Date'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Product Categories')


class Measure(models.Model):
    """
    Model Measure for Good
    """
    name = models.CharField(max_length=250, unique=True, verbose_name=_('Unit of measure'))
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('Date Added'))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('Editing Date'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Unit of measure')
        verbose_name_plural = _('Units of measurement')


class Packing(models.Model):
    """
    Model Packing for Good
    """
    name = models.CharField(max_length=250, blank=True, null=True, unique=True, verbose_name=_('Packaging Type'))
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('Date Added'))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('Editing Date'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Packaging Type')
        verbose_name_plural = _('Packaging types')


class Original(models.Model):
    """
    Model Original for Good
    """
    count = models.IntegerField(blank=True, null=True, unique=True, verbose_name=_('Quantity in the original'))
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('Date Added'))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('Editing Date'))

    def __str__(self):
        return str(self.count)

    class Meta:
        verbose_name = _('Quantity in the original')
        verbose_name_plural = _('Originality')


class Good(models.Model):
    """
    Model Good
    """
    name = models.OneToOneField(TradeName, on_delete=models.CASCADE, verbose_name=_('Product Name'))
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, verbose_name=_('Maker'))
    packing = models.ForeignKey(Packing,
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE,
                                verbose_name=_('Packaging Type'))
    original = models.ForeignKey(Original,
                                 blank=True,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('Originality'))
    photo = models.ImageField(blank=True, upload_to='good-logo', verbose_name=_('Photo'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE, verbose_name=_('Unit of measure'))
    description = models.TextField(max_length=250, blank=True, null=True, verbose_name=_('Description'))
    slug = models.SlugField(max_length=250, verbose_name=_('URL'), blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('Date Added'))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('Editing Date'))

    def __str__(self):
        return f'{self.category}: {self.name}'

    def save(self, *args, **kwargs): # pylint: disable=W0221
        self.slug = slugify(
            f'{self.name}-{self.maker}'
        )
        super(Good, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('name', 'maker', 'measure')
        verbose_name = _('Good')
        verbose_name_plural = _('Goods')
