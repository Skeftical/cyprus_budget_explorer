from django.shortcuts import render
from serializers import OfficeSerializer,SubOfficeSerializer
from rest_framework.views import APIView
from models import Office,SubOffice
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import operator
# Create your views here.

class OfficesList(APIView):
    """
    API endpoint that allows ministries to be retrieved.
    """
    def get(self, request, format=None):
        offices = Office.objects.all()
        serializer = OfficeSerializer(offices, many=True)
        return Response(serializer.data)


class SubOfficesList(APIView):
    """
    API endpoint that allows suboffices to be retrieved.
    """
    def get(self, request, officeId, format=None):
        offices = Office.objects.filter(officeId=officeId)
        #Way to execute an OR query
        q_list = [Q(office=x) for x in offices]
        query = q_list.pop()
        for item in q_list:
            query |= item

        suboffices = SubOffice.objects.filter(query)
        serializer = SubOfficeSerializer(suboffices, many=True)
        return Response(serializer.data)



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

