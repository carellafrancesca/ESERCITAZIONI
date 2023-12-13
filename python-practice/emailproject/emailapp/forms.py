from django import forms
#=> importa la classe forms dal modulo Django

class EmailForm(forms.Form):
    # EmailForm che eredita dalla classe forms.Form. => EmailForm è un tipo di form di Django.
    email = forms.EmailField(label="Email")
    # Il parametro label viene utilizzato per specificare l'etichetta del campo che verrà visualizzata nell'interfaccia utente.
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    # CharField è un campo per stringhe di testo