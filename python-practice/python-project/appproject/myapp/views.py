from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Listitem

# Create your views here.
def index(request):
    items = Listitem.objects.all()
    return render(request, 'myapp/index.html', {'items': items})

# Questa view recupera tutti gli oggetti ListItem dal database utilizzando ListItem.objects.all() e li passa al template HTML chiamato 'myapp/index.html' come contesto, con la chiave 'items'. Questo significa che all'interno del template, puoi accedere a questi oggetti utilizzando la variabile items.

def add_item(request):
    if request.method == 'POST':
        text = request.POST['item_text']
        Listitem.objects.create(text=text)
        return HttpResponseRedirect('/')
    
# Questa view gestisce le richieste POST provenienti da un form HTML. Se il metodo della richiesta è POST, estrai il testo dall'oggetto richiesta (request.POST['item_text']), quindi crea un nuovo oggetto ListItem nel database con quel testo utilizzando ListItem.objects.create(text=text). Successivamente, reindirizza l'utente alla pagina principale usando HttpResponseRedirect('/').
    
def search_items(request):
    query = request.GET.get('query', '')
    # La funzione search_items è la vista che gestisce la ricerca degli elementi. Prende la richiesta (request) come parametro e recupera il valore del parametro di query dalla stringa di query (GET) fornita nella richiesta.
    results = Listitem.objects.filter(text__icontains=query)
    # Qui, text__icontains=query indica di cercare la stringa di query (query) all'interno del campo text in modo case-insensitive (senza distinguere tra maiuscole e minuscole).
    return render(request, 'myapp/search_results.html', {'results': results, 'query': query})
    # La funzione render prende la richiesta, il nome del template e un dizionario di contesto. In questo caso, il contesto contiene i risultati della ricerca (results) e la query di ricerca (query), che saranno disponibili nel template per la visualizzazione.    