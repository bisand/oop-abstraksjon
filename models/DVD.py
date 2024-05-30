from models.Media import Media


class DVD(Media):
    def __init__(self, title, director, editor=None):
        super().__init__(title)
        self.director = director
        self.editor = editor
        self.type = "DVD"

    def display_info(self):
        if(self.editor is None):
            return f"Title: {self.title}, Author: {self.director}"
        else:
            return f"Title: {self.title}, Author: {self.director}, Editor: {self.editor}"

    def get_type(self):
        return "DVD"
