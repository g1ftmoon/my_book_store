from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.books.models import Book
from applications.books.serializers import BookSerializer\
# 1
# @api_view(['GET'])
# def book_list(request):
#     if request.method == 'GET':
#         categories = Book.objects.all()
#         serializer = BookSerializer(categories, many=True)
#         return Response(serializer.data)
# 2
# class BookView(APIView):
#     def get(self, request):
#         categories = Book.objects.all()
#         serializer = Book(categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
# # 3
# class BookListView(generics.ListApiView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
