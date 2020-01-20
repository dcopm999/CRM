from django.contrib import admin

from frontend_app import models


@admin.register(models.Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['good', 'title', 'created', 'edited']
