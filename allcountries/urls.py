from django.urls import path
from .views import allcountries_view
urlpatterns = [
    path('', allcountries_view.as_view()),

]