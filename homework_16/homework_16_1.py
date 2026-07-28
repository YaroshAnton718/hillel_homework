import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def _build_from_area(self, area):
        side1 = math.isqrt(int(area))

        if side1 == 0:
            side1 = 1

        side2 = area / side1

        return Rectangle(side1, side2)

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False

        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented

        new_area = self.get_square() + other.get_square()

        return self._build_from_area(new_area)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented

        new_area = self.get_square() * n

        return self._build_from_area(new_area)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print("OK")