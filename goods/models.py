"""
Goods.models
"""
from django.db import models

from pytils.translit import slugify

from addresses.models import Country


class Maker(models.Model):
    """
    Model Maker for Good
    """
    name = models.CharField(max_length=250, unique=True, verbose_name='Наименование производителя')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна производитель')
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата добавления')
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата редактирования')

    def __str__(self):
        return f'{self.name},{self.country}'

    class Meta:
        verbose_name = 'Производителя'
        verbose_name_plural = 'Производители'


class TradeName(models.Model):
    """
    Model TradeName for Good
    """
    name = models.CharField(max_length=250, unique=True, verbose_name='Наименование товара')
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата добавления')
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата редактирования')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Наименование товара'
        verbose_name_plural = 'Наименования товара'


class Category(models.Model):
    """
    Model Category for Good
    """
    name = models.CharField(max_length=250, unique=True, verbose_name='Название котегории')
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата добавления')
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата редактирования')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Котегория'
        verbose_name_plural = 'Котегории товара'


class Measure(models.Model):
    """
    Model Measure for Good
    """
    name = models.CharField(max_length=250, unique=True, verbose_name='Еденица измерения')
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата добавления')
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата редактирования')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Еденица измерения'
        verbose_name_plural = 'Еденицы измерения'


class Packing(models.Model):
    """
    Model Packing for Good
    """
    name = models.CharField(max_length=250, blank=True, null=True, unique=True, verbose_name="Тип упаковки")
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата добавления')
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата редактирования')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип упаковки'
        verbose_name_plural = 'Типы упаковки'


class Original(models.Model):
    """
    Model Original for Good
    """
    count = models.IntegerField(blank=True, null=True, unique=True, verbose_name="Кол-во в оригинале")
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата добавления')
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата редактирования')

    def __str__(self):
        return f'{self.count}'

    class Meta:
        verbose_name = 'Кол-во в оригинале'
        verbose_name_plural = 'Оригинальность'


class Good(models.Model):
    """
    Model Good
    """
    name = models.OneToOneField(TradeName, on_delete=models.CASCADE, verbose_name='Наименование товара')
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, verbose_name='Производитель')
    packing = models.ForeignKey(Packing, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Тип упаковки')
    original = models.ForeignKey(Original,
                                 blank=True,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 verbose_name='Оригинальность')
    photo = models.ImageField(blank=True, upload_to='good-logo', verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Котегория')
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE, verbose_name='Еденица измерения')
    description = models.TextField(max_length=250, blank=True, null=True, verbose_name='Описание')
    slug = models.SlugField(max_length=250, verbose_name="ЧПУ", blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата добавления')
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата редактирования')

    def __str__(self):
        return f'{self.name},{self.maker},{self.category}'

    def save(self, *args, **kwargs): # pylint: disable=W0221
        self.slug = slugify(
            f'{self.name}{self.maker}'
        )
        super(Good, self).save(*args, **kwargs)

    class Meta:
        unique_together = ("name", "maker", "measure")
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
