from django.shortcuts import render
from serializers import OfficeSerializer,SubOfficeSerializer
from rest_framework import viewsets
from models import Office,SubOffice

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class OfficeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Office.objects.filter(year=2014)
    serializer_class = OfficeSerializer


@api_view(['GET'])
def office_detail(request, officeId):
    """
    Retrieve, update or delete an office instance.
    """
    try:
        office = Office.objects.filter(officeId=officeId)
    except Office.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OfficeSerializer(office, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def office_suboffices(request, officeId, year):
    """
    Retrieve, update or delete an office instance.
    """
    try:
        suboffice = SubOffice.objects.filter(office=Office.objects.get(officeId=officeId, year=year))
    except Office.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubOfficeSerializer(suboffice, many=True)
        return Response(serializer.data)

def index(request):
    return render(request,'index.html')

