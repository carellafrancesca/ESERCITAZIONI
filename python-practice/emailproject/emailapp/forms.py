from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    # EmailForm è una sottoclasse di forms.ModelForm. Questo significa che stai creando un form che è basato su un modello esistente (nel tuo caso, il modello Email).
    class Meta:
        model = Email
        fields = ['email', 'subject', 'message']

# class Meta => dentro la classe EmailForm, la classe Meta viene utilizzata per fornire metadati relativi al form.

# model = Email => specifica il modello del database associato a questo form. In questo caso, il form EmailForm è associato al modello Email.

# fields = ['email', 'subject', 'message'] => specifica quali campi del modello devono essere inclusi nel form.