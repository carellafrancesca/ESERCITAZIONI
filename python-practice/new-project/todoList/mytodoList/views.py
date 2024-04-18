from django.shortcuts import render, redirect
from .models import ListItem
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    items = ListItem.objects.all()
    return render(request, 'todotemplates/index.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        text = request.POST['item_text'] # se il metodo della richiesta è POST, allora estrae il testo dalla richiesta
        ListItem.objects.create(text=text) # viene creato un oggetto ListItem dal testo estratto precedentemente
        return HttpResponseRedirect('/')
    
#def delete_items(request):
    
    #if request.method == 'POST':
    #    text_to_delete = request.POST['item_text'] # ottieni il testo dell'elemento da eliminare dalla richiesta POST
    #    try: 
    #        items_to_delete = ListItem.objects.get(text = text_to_delete)
    #        items_to_delete.delete()
    #    except ListItem.DoesNotExist: # controlla se l'elemento da cancellare esiste nella lista
    #        pass
    #return redirect('index')

def search_items(request):
    query = request.GET.get('query', '') # recupera il valore del parametro di query dalla stringa di query
    results = ListItem.objects.filter(text__icontains=query) # text__icontains=query indica di cercare la stringa di query (query) all'interno del campo text in modo case-insensitive
    return render(request, 'todotemplates/search_results.html', {'results':results, 'query':query}) # render prende i risultati della ricerca (results) e la query di ricerca (query), che verranno poi visualizzate nel template specificato

