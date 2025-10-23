
class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'[{self._x}, {self._y}]'
    
    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

# ----------------------------------

a = Vector(6, 0)
b = Vector(3, 4)

print(a)
print(b)

c = a + b

print(c)