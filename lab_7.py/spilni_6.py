import math

def rectangle_area_with_circles(a, b, d1, d2, d3, d4):
    total_area = a * b

    r1 = d1 / 2
    r2 = d2 / 2
    r3 = d3 / 2
    r4 = d4 / 2
    circle_area1 = math.pi * (r1 ** 2)
    circle_area2 = math.pi * (r2 ** 2)
    circle_area3 = math.pi * (r3 ** 2)
    circle_area4 = math.pi * (r4 ** 2)

    final_area = total_area - (circle_area1 + circle_area2 + circle_area3 + circle_area4)
    return final_area

a = 10
b = 6
d1 = 4
d2 = 2
d3 = 5
d4 = 3

area = rectangle_area_with_circles(a, b, d1, d2, d3, d4)
print("Площа прямокутної заготовки з вирізаними кругами:", area)
