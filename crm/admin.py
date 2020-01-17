from django.contrib import admin
from crm.models import AgreementStatus, Agreement

@admin.register(AgreementStatus)
class AgreementStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'edited']

@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = ['code', 'status', 'result', 'created', 'edited']
    list_filter = ['code', ]
