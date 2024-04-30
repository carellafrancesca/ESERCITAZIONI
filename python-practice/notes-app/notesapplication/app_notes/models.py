from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name
    
class Note(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # on_delete=models.CASCADE fa si che la riga intera verrà eliminata se ForeignKey viene eliminata
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title