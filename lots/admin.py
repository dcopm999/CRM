from django.contrib import admin
from . import models

@admin.register(models.Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = ['lot_number']

@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name']