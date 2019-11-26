from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Pothole(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    imageNames = models.CharField(max_length=100,default=None,null=True)

class JsonFile(models.Model):
    jsonfile = models.FileField(upload_to="static")
