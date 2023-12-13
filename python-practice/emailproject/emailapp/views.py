from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm

# Create your views here.

def send_email(request):
    # Vista Django chiamata send_email, che gestisce l'invio di email utilizzando il form EmailForm.
    if request.method == 'POST': # Per controllare se la richiesta fatta sia una POST
        form = EmailForm(request.POST)
        # Si istanzia il form EmailForm passando i dati ricevuti nella richiesta POST per popolare il form
        if form.is_valid(): # Controllare la validità del form
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # Se il form è valido, vengono estratti i dati puliti (cleaned_data) dal form. Questi dati sono già stati validati e sono sicuri da utilizzare.

            send_mail(subject, message, 'your_email@example.com', [email])
            # 'your_email@example.com'=> l'indirizzo email del mittente. 
            # [email] => destinatario dell'email, [] per indicare che possono esserci più destinatari

            return render(request, 'emailapp/email_sent.html')
    else:
        form = EmailForm()
        # Viene creato un oggetto vuoto

    return render(request, 'emailapp/send_email.html', {'form': form})
    # viene restituita una risposta HTTP che renderizza il template 'emailapp/send_email.html'. Questa volta, viene passato anche il form vuoto come contesto al template, in modo che il form possa essere visualizzato nella pagina HTML.

# render: È una funzione di Django che rende il contenuto di un template HTML in una risposta HTTP.
# request: Questo è l'oggetto di richiesta HTTP che viene passato alla vista come parametro. Contiene informazioni sulla richiesta del client, come i dati del form (nel caso in cui sia una richiesta POST) e altri dettagli.
# 'emailapp/send_email.html': Questo è il percorso del template HTML che sarà renderizzato. In questo caso, emailapp/send_email.html indica a Django di cercare un file HTML chiamato send_email.html nella directory emailapp.
# {'form': form}: Questo è un dizionario che contiene il contesto che viene passato al template. Il contesto è composto da variabili che saranno disponibili nel template. Nel tuo caso, stai passando una variabile chiamata form che rappresenta l'oggetto del form creato nella tua vista.