from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Office(models.Model):
    officeId = models.CharField(max_length=10)
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    total = models.DecimalField(decimal_places=3, max_digits=18)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name


class SubOffice(models.Model):
    office = models.ForeignKey(Office)
    subOfficeId = models.IntegerField()
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    total = models.DecimalField(decimal_places=3, max_digits=18)
    pagio = models.DecimalField(decimal_places=3, max_digits=18, null=True)
    taktikes = models.DecimalField(decimal_places=3, max_digits=18, null=True)
    anaptuksiakes = models.DecimalField(decimal_places=3, max_digits=18, null=True)
    approved = models.NullBooleanField(null=True)
    revised = models.NullBooleanField(null=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name