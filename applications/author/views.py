from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.author.models import Author
from applications.author.serializers import AuthorSerializer
#  # 1
# @api_view(['GET'])
# def author_list(request):
#     if request.method == 'GET':
#         categories = Author.objects.all()
#         serializer = Author(categories, many=True)
#         return Response(serializer.data)

# #2
# class AuthorView(APIView):
#     def get(self, request):
#         categories = Author.objects.all()
#         serializer = Author(categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# # 3
# class AuthorListView(generics.ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
