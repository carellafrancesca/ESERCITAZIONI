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