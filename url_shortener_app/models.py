from django.db import models
import socket
import json
import re
from urllib.request import urlopen 
from django.contrib.gis.geoip2 import GeoIP2
import geoip2.database

# Create your models here.
class LongToShort(models.Model):
    longurl = models.URLField(max_length=250)
    shorturl = models.CharField(max_length=25, unique=True)
    visit_count = models.IntegerField(default = 1)
    city = models.CharField(max_length=25, default = 'India')
    long = models.DecimalField(max_digits=8, decimal_places=3, default = 0)
    lat = models.DecimalField(max_digits=8, decimal_places=3, default = 0)
    ip_address = models.CharField(max_length=50, default = '127.0.0.1')
    
