class Calculator:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b


calc = Calculator()
print(calc.add(1, 2))
print(calc.add(1, 2, 3))

