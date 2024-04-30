from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_note, name='create_note'),
    path('note/<int:pk>/edit/', views.edit_note, name='edit_note'),
    path('note/<int:pk>/delete/', views.delete_note, name='delete_note'),
    path('category/<int:pk>/delete/', views.delete_category, name='delete_category'),
]