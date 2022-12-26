import requests
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response

class statistics_view(APIView):
    def get(self, request):
        url = "https://api.covid19api.com/world/total"
        payload={}
        headers = {}   
        response = requests.request("GET", url, headers=headers, data=payload) 
        if response.status_code == 200:
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
