from models.Vehicle import Vehicle


class Lorry(Vehicle):
    def __init__(self, make, model) -> None:
        super().__init__(make, model)

    def loading_capacity(self):
        return "This lorry har a huge loading capacity!"