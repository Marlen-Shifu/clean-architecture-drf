from abc import ABC, abstractmethod
from typing import List, Optional
from apps.book_catalogs.domains.entities.books_catalogs import BookEntity, ReviewEntity


class AbstractBookRepository(ABC):

    @abstractmethod
    def list_books(self) -> List[BookEntity]:
        ...

    @abstractmethod
    def get_book(self, book_id) -> Optional[BookEntity]:
        ...

    @abstractmethod
    def get_book_reviews(self, book_id) -> List[ReviewEntity]:
        ...
