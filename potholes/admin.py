from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Pothole

@admin.register(Pothole)
class PotholeAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
