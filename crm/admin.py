from django.contrib import admin
from crm.models import AgreementTask, TaskStatus, Agreement, AgreementItem


class AgreementItemInline(admin.TabularInline):
    model = AgreementItem

class AgreementTaskInline(admin.TabularInline):
    model = AgreementTask

@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'edited']


@admin.register(AgreementTask)
class AgreementTaskAdmin(admin.ModelAdmin):
    list_display = ['contragent', 'status', 'created', 'date', 'is_active']
    date_hierarchy = 'date'
    list_filter = ['status', ]
    search_fields = ['agreement__contragent', ]
    list_filter = ['status__name', ]


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    inlines = [AgreementItemInline, AgreementTaskInline]
    list_display = ['contragent', 'result', 'created', 'edited']
    list_filter = ['result', ]
    search_fields = ['contragent__name', ]
