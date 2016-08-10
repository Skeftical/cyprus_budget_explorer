from rest_framework import serializers
from models import Office,SubOffice

class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office
        fields = ('officeId', 'name', 'year', 'total', 'approved', 'revised')
class SubOfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubOffice
        fields = ('subOfficeId', 'name', 'year', 'total', 'pagio', 'taktikes', 'anaptuksiakes', 'approved', 'revised')