from math import pi, hypot


class Kolo:
    def __init__(self, x, y, r) -> None:
        self.x = x
        self.y = y
        self.radius = r

    def area(self):
        return pi * self.radius**2

    def len(self):
        return 2 * pi * self.radius

    def sector(self, angle):
        return self.area() * angle / 360

    def dot_in_kolo(self, a, b):
        dist = hypot(self.x, self.y, a, b)
        return dist <= self.radius


k = Kolo(0, 0, 10)
alpha = 180
dot = (7, 7)

print(f"Довжина кола: {k.len():.3f}")
print(f"Площа кола: {k.area():.3f}")
print(f"Площа сектора кола: {k.sector(angle=alpha):.3f}")
print(f"Приналежності точки з координатами {dot}: {k.dot_in_kolo(*dot)}")