from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Category
from .forms import NoteForm, CategoryForm
from django.utils import timezone

# Create your views here.
def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_name = request.POST.get('category')
        # per trovare il valore associato alle parole chiave specificate; se trova il valore, restituirà il suo contenuto

        if category_name:
            category, created = Category.objects.get_or_create(category_name=category_name)
            pub_date = timezone.now()
            note = Note.objects.create(title=title, content=content, category=category, publication_date=pub_date)
            return redirect('create_note')
        else:
            pass
    else:
        form = NoteForm()
        notes = Note.objects.all()
        categories = Category.objects.all()

    if 'category' in request.GET:
        category_id = request.GET['category']
        notes = Note.objects.filter(category_id=category_id)
    else:
       notes = Note.objects.all()
        # per controllare se il parametro 'category' è presente nella richiesta GET; se presente, estrae l'ID della categoria dalla richiesta GET e filtra le note in base a questo ID di categoria (filter) altrimenti restituisce tutte le note
    return render(request, 'notes-template/notes_page.html', {'form': form, 'notes': notes, 'categories': categories})

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('create_note')
        else:
            form = NoteForm(instance=note)
    return render(request, 'notes-template/edit_note.html', {'form': form})
# l'ultilizzo di 'instance' consente di lavorare facilmente con dati esistenti e di precompilare un form con i valori di un'istanza del modello

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('create_note')

def delete_category(request, pk):
    note = get_object_or_404(Category, pk=pk)
    note.delete()
    return redirect('create_note')