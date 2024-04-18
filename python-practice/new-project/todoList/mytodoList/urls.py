from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_item, name='add_item'),
    #path('delete/<str:item_text>/', views.delete_items, name='delete_items'), # serve aggiungere informazioni sull'elemento da eliminare
    path('search/', views.search_items, name='search_items'),
]