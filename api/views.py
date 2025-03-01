# from django.shortcuts import render
# from django.http import JsonResponse
# from .serializers import BookSerializer
# from .models import Book

# def index(request):
#     return JsonResponse({'message':'Hello World!'})

# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe=201)
#     return JsonResponse(serializer.data, safe=400)


from rest_framework import viewsets,filters
from .models import Book, author
from .serializers import BookSerializer, authorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = author.objects.all()
    serializer_class = authorSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'birth_date', 'country'] #champ de recherche
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title', 'author'] #champ de recherche