from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
from .fetchApi import fetchdata
from .serializers import bookserializer
from django.http import HttpResponse


@api_view(['GET'])
def fetch(request):
    api_data = fetchdata()

    for i in api_data['books']:
        serializer= bookserializer(data =i)

        if serializer.is_valid():
            serializer.save()

        else:
            return Response({'Error'})
        
    return Response({'Data Saved in DB'})

    


def home(requests):
    return HttpResponse("go to /fetch to fetch api data")





