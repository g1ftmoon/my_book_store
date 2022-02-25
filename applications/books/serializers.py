from applications.author import serializers
from applications.books.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        field = '__all__'
