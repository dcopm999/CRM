"""
Goods.admin
"""
from django.contrib import admin

from goods import models


@admin.register(models.Maker)
class MakerAdmin(admin.ModelAdmin):
    """
    Maker for admin page
    """
    model = models.Maker
    list_display = ['name', 'country']


@admin.register(models.Packing)
class PackingAdmin(admin.ModelAdmin):
    """
    Packing for admin page
    """
    model = models.Packing
    list_display = ['name']


@admin.register(models.Original)
class OriginalAdmin(admin.ModelAdmin):
    """
    Original for admin page
    """
    model = models.Original
    list_display = ['count']


@admin.register(models.TradeName)
class TradeNameAdmin(admin.ModelAdmin):
    """
    TradeName for admin page
    """
    model = models.TradeName
    list_display = ['name']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category for admin page
    """
    model = models.Category
    list_display = ['name']


@admin.register(models.Measure)
class MeasureAdmin(admin.ModelAdmin):
    """
    Measure for admin page
    """
    model = models.Measure
    list_display = ['name']


@admin.register(models.Good)
class GoodAdmin(admin.ModelAdmin):
    """
    Good for admin page
    """
    model = models.Good
    list_display = ['name', 'maker', 'category', 'measure']
