from django.urls import path
from .views import country_data_view

urlpatterns = [
    path('', country_data_view.as_view()),
]