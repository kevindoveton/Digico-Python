from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SD9(models.Model):
	aux1Values = models.CharField(max_length=1000)
	inputNames = models.CharField(max_length=1000)
	aux2Values = models.CharField(max_length=1000)
	aux3Values = models.CharField(max_length=1000)
	aux4Values = models.CharField(max_length=1000)
	aux5Values = models.CharField(max_length=1000)
	aux6Values = models.CharField(max_length=1000)
	aux7Values = models.CharField(max_length=1000)
	aux8Values = models.CharField(max_length=1000)
	aux9Values = models.CharField(max_length=1000)
	aux10Values = models.CharField(max_length=1000)
	aux11Values = models.CharField(max_length=1000)
	aux12Values = models.CharField(max_length=1000)
