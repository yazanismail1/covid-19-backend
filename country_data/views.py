import requests
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response

class country_data_view(APIView):
    def get(self, request):
        country = self.request.query_params.get('country_name')
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')
        url = f"https://api.covid19api.com/country/{country}/status/confirmed?from={from_date}&to={to_date}"
        payload={}
        headers = {}   
        response = requests.request("GET", url, headers=headers, data=payload) 
        if response.status_code == 200:
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)

