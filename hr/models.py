from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey


class Department(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=50, verbose_name=_('Department'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')


class Employee (models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name=_("Department"))
    first_name = models.CharField(max_length=50, verbose_name=_("First name"))
    middle_name = models.CharField(max_length=50, verbose_name=_("Middle name"))
    last_name = models.CharField(max_length=50, verbose_name=_("Last name"))
    phone = models.CharField(max_length=200, verbose_name=_("Phone number"), null=True, blank=True)
    position = models.CharField(max_length=50, verbose_name=_("Position"))
    role = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Role"))
    birthday = models.DateField(blank=True, null=True, verbose_name=_("Birth day"))
    created = models.DateTimeField(auto_now_add=True, editable=False,  verbose_name=_("Created"))
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name=_("Edited"))
    
    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
    
    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")