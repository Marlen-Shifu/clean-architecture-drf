from rest_framework import serializers
from apps.book_catalogs.domains.entities.books_catalogs import GenreEntity, AuthorEntity, BookEntity, ReviewEntity

class GenreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class ReviewSerializer(serializers.Serializer):
    rating = serializers.IntegerField()
    review_text = serializers.CharField()

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    genre = GenreSerializer()
    author = AuthorSerializer()
    publication_date = serializers.DateField()
    average_rating = serializers.FloatField()

class BookDetailSerializer(BookSerializer):
    reviews = ReviewSerializer(many=True)
