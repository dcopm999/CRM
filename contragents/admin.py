from django.contrib import admin

from contragents import models

class ContactInline(admin.TabularInline):
    model = models.Contact

@admin.register(models.Contragent)
class ContragentAdmin(admin.ModelAdmin):
    inlines = [ContactInline, ]
    list_display = ['name', 'inn', 'address_ur']

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'middle_name', 'contragent']
