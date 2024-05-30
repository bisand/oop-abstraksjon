from models.Media import Media


class Magazine(Media):
    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number
        self.type = "Magazine"

    def display_info(self):
        return f"Title: {self.title}, Issue Number: {self.issue_number}"

    def get_type(self):
        return "Magazine"
    