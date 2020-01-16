'''
package: stocks
description: admin
'''
from django.contrib import admin
from . import models

@admin.register(models.Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = ['lot_number', 'total_price']
