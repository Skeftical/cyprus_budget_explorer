from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Office(models.Model):
    officeId = models.CharField(max_length=10)
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    total = models.DecimalField(decimal_places=3, max_digits=18)
    approved = models.BooleanField(default=False)
    revised = models.BooleanField(default=False)
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name


class SubOffice(models.Model):
    office = models.ForeignKey(Office)
    subOfficeId = models.CharField(max_length=6)
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    total = models.DecimalField(decimal_places=3, max_digits=18)
    pagio = models.DecimalField(decimal_places=3, max_digits=18, null=True)
    taktikes = models.DecimalField(decimal_places=3, max_digits=18, null=True)
    anaptuksiakes = models.DecimalField(decimal_places=3, max_digits=18, null=True)
    approved = models.BooleanField(default=False)
    revised = models.BooleanField(default=False)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name