from django.contrib import admin
from crm.models import AgreementTask, TaskStatus, Agreement


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'edited']


@admin.register(AgreementTask)
class AgreementTaskAdmin(admin.ModelAdmin):
    list_display = ['status', 'created', 'edited']


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = ['code', 'result', 'created', 'edited']
    list_filter = ['code', ]
