from django.db import models
# => importa la classe forms dal modulo Django

# Create your models here.

class Email(models.Model):
    # Email che eredita dalla classe models.Model
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.subject
    
    # Il metodo __str__ è un metodo speciale in Python che viene invocato quando si cerca di ottenere una rappresentazione leggibile dell'oggetto sotto forma di stringa. Questo metodo restituisce una stringa che dovrebbe essere una rappresentazione testuale significativa dell'oggetto.

    # Il metodo __str__ è un metodo speciale in Python che viene invocato quando si cerca di ottenere una rappresentazione leggibile dell'oggetto sotto forma di stringa. Questo metodo restituisce una stringa che dovrebbe essere una rappresentazione testuale significativa dell'oggetto.