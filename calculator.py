

class Calculator:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    
    def multiply(self):
        return self._x * self._y

    def add(self):
        return self._x + self._y

    def modulus(self):
        try:
            if self._y == 0:
                raise ZeroDivisionError
        except ZeroDivisionError as err:
            print('Cannot divide by zero')
        else:
            return self._x % self._y
    
    def subtract(self):
        return self._x - self._y
    
    def divide(self):
        try:
            if self._y == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            pass
        else:
            return self._x / self._y