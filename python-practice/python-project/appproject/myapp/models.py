from django.db import models

# Create your models here.
class Listitem(models.Model):
    # Qui stai creando una nuova classe chiamata ListItem che eredita dalla classe Model di Django. Questo indica che ListItem è un modello del database Django.
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
    
    # Questo metodo è definito per rappresentare un'istanza del modello come una stringa. In questo caso, restituisce la rappresentazione testuale dell'oggetto ListItem, che è il valore del campo text. Questo metodo è utile per la visualizzazione leggibile degli oggetti nei log o nell'interfaccia amministrativa di Django.