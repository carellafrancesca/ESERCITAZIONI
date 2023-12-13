from django.urls import path
# importa la classe path dal modulo django.urls.
from .views import send_email
#  La parte views di un'app Django è generalmente responsabile della logica di presentazione, gestendo le richieste HTTP e generando le risposte.

urlpatterns = [
    path('send_email/', send_email, name='send_email'),
]

# 'send_email/': Questa è la parte dell'URL che il framework cerca di corrispondere quando una richiesta viene fatta al tuo sito. 
# send_email: Questo è il nome della funzione della vista (nel file views.py) che gestirà la richiesta quando il percorso corrisponderà.
# name='send_email': Questo è il nome assegnato a questa regola di routing. Può essere utilizzato per fare riferimento a questa regola specifica all'interno del tuo codice Django, ad esempio, quando generi URL dinamicamente nei tuoi template.