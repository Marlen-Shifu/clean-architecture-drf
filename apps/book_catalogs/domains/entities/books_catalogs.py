
class GenreEntity:
    def __init__(self, name):
        self.name = name

class AuthorEntity:
    def __init__(self, name):
        self.name = name

class BookEntity:
    def __init__(self, id, title, genre, author, publication_date, average_rating=0):
        self.id = id
        self.title = title
        self.genre = genre
        self.author = author
        self.publication_date = publication_date
        self.average_rating = average_rating

    def set_average_rating(self, average_rating):
        if average_rating < 0 or average_rating > 5:
            raise ValueError('Average rating must be between 0 and 5')
        self.average_rating = average_rating

    def set_reviews(self, reviews):
        self.reviews = reviews

class ReviewEntity:

    rating_available_values = [1, 2, 3, 4, 5]

    def __init__(self, rating, review_text, book=None):
        self.book = book
        self.review_text = review_text

        if rating not in self.rating_available_values:
            raise ValueError(f'Rating must be one of {self.rating_available_values}')
        self.rating = rating
