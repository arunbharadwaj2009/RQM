from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Pothole
from django.utils.html import format_html

@admin.register(Pothole)
class PotholeAdmin(OSMGeoAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50px" />'.format("/static/Gir_Arun.jpg"))

    image_tag.short_description = 'Image' 

    list_display = ('name', 'location', "image_tag")
