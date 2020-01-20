from django.contrib import admin
from . import models

@admin.register(models.Pricing)
class PricingModelAdmin(admin.ModelAdmin):
    list_display = ['name']

