from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin


from contragents import models
from crm.models import Agreement

'''
class AgreementInline(admin.TabularInline):
    model = Agreement
    fields = ['code', 'result']
'''

class ContactResource(resources.ModelResource):
    class Meta:
        model = models.Contact

class ContragentResource(resources.ModelResource):
    class Meta:
        model = models.Contragent

class ContactInline(admin.TabularInline):
    model = models.Contact

@admin.register(models.Contragent)
class ContragentAdmin(ImportExportModelAdmin):
    inlines = [ContactInline, ]
    resource_class = ContragentResource
    list_display = ['name', 'inn', 'address_ur']
    search_fields = ['name', 'inn']
    list_filter = ['contragent_type', ]


@admin.register(models.Contact)
class ContactAdmin(ImportExportModelAdmin):
    resource_class = ContactResource
    list_display = ['last_name', 'first_name', 'middle_name', 'contragent']
