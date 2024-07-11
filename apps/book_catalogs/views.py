from rest_framework import viewsets
from rest_framework.response import Response

from apps.book_catalogs.factories import get_book_repository
from apps.book_catalogs.serializers import BookSerializer, BookDetailSerializer
from apps.book_catalogs.use_cases.books_catalogs import GetBooksUseCase, GetBookUseCase


class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        book_repository = get_book_repository()
        use_case = GetBooksUseCase(book_repository)
        books = use_case.list_books()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        book_repository = get_book_repository()
        use_case = GetBookUseCase(book_repository)
        book = use_case.get_book(pk)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)
