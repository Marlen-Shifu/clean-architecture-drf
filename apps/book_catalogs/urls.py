from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookViewSet

books_router = DefaultRouter()
books_router.register(prefix='', viewset=BookViewSet, basename='books')

urlpatterns = [
    path('', include(books_router.urls)),
]
