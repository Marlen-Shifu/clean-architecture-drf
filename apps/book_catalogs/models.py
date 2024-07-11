from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
