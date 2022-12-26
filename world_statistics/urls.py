from django.urls import path
from .views import statistics_view

urlpatterns = [
    path('', statistics_view.as_view()),
]