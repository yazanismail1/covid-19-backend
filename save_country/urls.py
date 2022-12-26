from django.urls import path
from .views import countires_list, country_detail

urlpatterns = [
    path('', countires_list),
    path('<int:pk>', country_detail),
]