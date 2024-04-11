def area_of_quadrilateral(a, b, c, d, diagonal):
    s = (a + b + c + d) / 2  
    area = (s - a) * (s - b) * (s - c) * (s - d) - (a * c + b * d - diagonal ** 2) ** 2 / 16
    return area ** 0.5  

a = float(input("Введіть довжину першої сторони: "))
b = float(input("Введіть довжину другої сторони: "))
c = float(input("Введіть довжину третьої сторони: "))
d = float(input("Введіть довжину четвертої сторони: "))
diagonal = float(input("Введіть довжину діагоналі: "))

result = area_of_quadrilateral(a, b, c, d, diagonal)

print("Площа чотирикутника:", result)
