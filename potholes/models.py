from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Pothole(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    #img = models.ImageField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def image_tag(self):
        from django.utils.html import escape
        return u'<img src="%s" />' % escape(<URL to the image>)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
