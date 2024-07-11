from apps.book_catalogs.interfaces.repositories.book_repository import AbstractBookRepository

class GetBooksUseCase:
    def __init__(self, repository: AbstractBookRepository):
        self.repository = repository

    def list_books(self):
        books = self.repository.list_books()
        for book in books:
            book.average_rating = self.get_book_average_rating(book.id)
        return books

    def get_book_average_rating(self, book_id):
        reviews = self.repository.get_book_reviews(book_id)
        if not reviews:
            return 0
        return sum(review.rating for review in reviews) / len(reviews)

class GetBookUseCase:
    def __init__(self, repository: AbstractBookRepository):
        self.repository = repository

    def get_book(self, book_id):
        book = self.repository.get_book(book_id)
        book_reviews = self.repository.get_book_reviews(book_id)
        book.set_average_rating(self.get_book_average_rating(book_id))
        book.set_reviews(book_reviews)
        return book

    def get_book_average_rating(self, book_id):
        reviews = self.repository.get_book_reviews(book_id)
        if not reviews:
            return 0
        return sum(review.rating for review in reviews) / len(reviews)
