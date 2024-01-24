from django.urls import path
from .views import saluta

urlpatterns = [
    path('saluta/', saluta, name='saluta')
]