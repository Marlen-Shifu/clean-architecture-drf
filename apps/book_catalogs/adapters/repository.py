from typing import List

from rest_framework.exceptions import NotFound

from apps.book_catalogs.domains.entities.books_catalogs import BookEntity, ReviewEntity
from apps.book_catalogs.interfaces.repositories.book_repository import AbstractBookRepository
from apps.book_catalogs.models import Book, Review


class BookRepository(AbstractBookRepository):
    def list_books(self) -> List[BookEntity]:
        return [
            BookEntity(
                id=book.id,
                title=book.title,
                genre=book.genre,
                author=book.author,
                publication_date=book.publication_date,
            )
            for book in Book.objects.all()
        ]

    def get_book(self, book_id):
        db_book = Book.objects.filter(id=book_id).first()
        if not db_book:
            raise NotFound()
        return BookEntity(
                id=db_book.id,
                title=db_book.title,
                genre=db_book.genre,
                author=db_book.author,
                publication_date=db_book.publication_date,
            )

    def get_book_reviews(self, book_id):
        reviews = Review.objects.filter(book_id=book_id)
        return [
            ReviewEntity(
                rating=review.rating,
                review_text=review.review_text,
            )
            for review in reviews
        ]
