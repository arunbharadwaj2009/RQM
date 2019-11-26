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
            html += '<a href="{}" target="_blank"><img src="{}" width="24px" /></a>'.format(
                "/static/" + imageName, "/static/" + imageName)
        return format_html(html)

    image_tag.short_description = 'Images'

    list_display = ('name', 'location', "image_tag")
