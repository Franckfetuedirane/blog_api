from rest_framework import serializers
from .models import Book, author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class authorSerializer(serializers.ModelSerializer):
    class Meta:
        model = author
        fields = '__all__'
