from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Office(models.Model):
    id = models.IntegerField()
    name = models.CharField()
    year = models.IntegerField()
    total = models.DecimalField()


class SubOffice(models.Model):
    id = models.IntegerField()
    name = models.CharField()
    year = models.IntegerField()
    total = models.DecimalField()
    pagio = models.DecimalField()
    taktikes = models.DecimalField()
    anaptuksiakes = models.DecimalField()
    approved = models.BooleanField()
    revised = models.BooleanField()