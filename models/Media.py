class Media:
    def __init__(self, title):
        self.title = title
        self.type = "Media"

    def display_info(self):
        return f"Title: {self.title}"

    def get_type(self):
        return self.type