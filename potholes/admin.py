from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Pothole
from django.utils.html import format_html

@admin.register(Pothole)
class PotholeAdmin(OSMGeoAdmin):

    def image_tag(self, obj):
        html = ""
        for imageName in obj.imageNames.split("|"):
            html += '<img src="{}" width="24px" />'.format("/static/"+ imageName)
        return format_html(html)        

    image_tag.short_description = 'Images' 

    list_display = ('name', 'location', "image_tag")
