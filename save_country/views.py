from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Country
from .serializers import *

@api_view(['GET', 'POST'])
def countires_list(request):
    if request.method == 'GET':
        data = Country.objects.all()

        serializer = CountrySerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def country_detail(request, pk):
    try:
        country = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)