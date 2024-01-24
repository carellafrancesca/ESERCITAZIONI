from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_item, name='add_item'),
]

# In questa lista urlpatterns, stai associando percorsi specifici alle tue views. Ogni elemento della lista è una chiamata a path che definisce il percorso dell'URL, la view associata e un nome per l'URL.

# path('', views.index, name='index'): Questo assegna la view views.index al percorso principale ('' rappresenta la radice del sito). Il nome dell'URL è definito come 'index', che può essere utilizzato nei template per generare URL in modo dinamico.

# path('add/', views.add_item, name='add_item'): Questo assegna la view views.add_item al percorso 'add/'. Anche in questo caso, è definito un nome per l'URL chiamato 'add_item'.