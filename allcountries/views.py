import requests
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class allcountries_view(APIView):
    def get(self, request):
        url = "https://api.covid19api.com/summary"
        payload={}
        headers = {}   
        response = requests.request("GET", url, headers=headers, data=payload) 
        if response.status_code == 200:
            data = response.json()
            countries = data["Countries"]
            cleaned_data = [
                {"Country":data["Country"], 
                "TotalConfirmed":data["TotalConfirmed"],
                "TotalDeaths": data["TotalDeaths"],
                "TotalRecovered": data["TotalRecovered"],
                "Date": data["Date"]} for data in countries]
            return Response(cleaned_data, status=status.HTTP_200_OK)

