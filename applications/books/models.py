
from django.db import models

from applications.author.models import Author




class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')
    title = models.CharField(max_length=255)
    date_of_publish = models.DateTimeField(auto_created='')
    picture = models.ImageField(upload_to='')
    price = models.DecimalField(max_digits=5, decimal_places=1)
    is_bestseller = models.BooleanField()

    def __str__(self):
        return self.title
    