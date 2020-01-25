from django.contrib import admin

from pricing import models


@admin.register(models.Pricing)
class PricingModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name']