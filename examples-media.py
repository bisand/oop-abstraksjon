class Media:
    def __init__(self, title):
        self.title = title

    def display_info(self):
        return f"Title: {self.title}"


class Book(Media):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}"


class DVD(Media):
    def __init__(self, title, director, editor=None):
        super().__init__(title)
        self.director = director
        self.editor = editor

    def display_info(self):
        if(self.editor is None):
            return f"Title: {self.title}, Author: {self.director}"
        else:
            return f"Title: {self.title}, Author: {self.director}, Editor: {self.editor}"


class Magazine(Media):
    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number

    def display_info(self):
        return f"Title: {self.title}, Issue Number: {self.issue_number}"


def display_media_info(media: Media):
    print(media.display_info())


book = Book("The Hobbit", "Tolkien")
dvd = DVD("The 5th element", "Luc Besson")
dvd2 = DVD("The 5th element", "Luc Besson", "John Doe")
magazine = Magazine("Time Magazine", "2024-05")

display_media_info(book)
display_media_info(dvd)
display_media_info(dvd2)
display_media_info(magazine)
