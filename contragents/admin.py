from django.contrib import admin

from contragents import models
from crm.models import Agreement

'''
class AgreementInline(admin.TabularInline):
    model = Agreement
    fields = ['code', 'result']
'''

class ContactInline(admin.TabularInline):
    model = models.Contact

@admin.register(models.Contragent)
class ContragentAdmin(admin.ModelAdmin):
    inlines = [ContactInline, ]
    list_display = ['name', 'inn', 'address_ur']
    search_fields = ['name', 'inn']
    list_filter = ['contragent_type', ]


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'middle_name', 'contragent']
