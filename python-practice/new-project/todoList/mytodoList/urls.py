from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_item, name='add_item'),
    #path('delete/', views.delete_items, name='delete_items'),
    path('search/', views.search_items, name='search_items'),
]