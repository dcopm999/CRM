from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from hr.models import Department, Employee

class EmployeeInline(admin.TabularInline):
    model = Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['position', 'last_name', 'first_name', 'middle_name']    

@admin.register(Department)
class DepartmentAdmin(DraggableMPTTAdmin):
    inlines = [EmployeeInline, ]
    list_display_name = ['name']



