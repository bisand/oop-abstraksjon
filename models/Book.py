from models.Media import Media


class Book(Media):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
        self.type = "Book"

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}"

    def get_type(self):
        return "Book"
