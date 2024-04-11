def find_intersection(a1, b1, c1, a2, b2, c2):
    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x, y
    else:
        return None

def find_triangle_area(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    intersection1 = find_intersection(a1, b1, c1, a2, b2, c2)
    intersection2 = find_intersection(a1, b1, c1, a3, b3, c3)
    intersection3 = find_intersection(a2, b2, c2, a3, b3, c3)
    if intersection1 and intersection2 and intersection3:
        x1, y1 = intersection1
        x2, y2 = intersection2
        x3, y3 = intersection3
        a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
        c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area
    else:
        return None

a1 = float(input("Введіть коефіцієнт a1: "))
b1 = float(input("Введіть коефіцієнт b1: "))
c1 = float(input("Введіть коефіцієнт c1: "))
a2 = float(input("Введіть коефіцієнт a2: "))
b2 = float(input("Введіть коефіцієнт b2: "))
c2 = float(input("Введіть коефіцієнт c2: "))
a3 = float(input("Введіть коефіцієнт a3: "))
b3 = float(input("Введіть коефіцієнт b3: "))
c3 = float(input("Введіть коефіцієнт c3: "))

area = find_triangle_area(a1, b1, c1, a2, b2, c2, a3, b3, c3)
if area is not None:
    print("Площа трикутника:", area)
else:
    print("Трикутник не існує або виникла помилка.")
