def tocka_pretinu(x1, y1, x2, y2, x3, y3):
    x = (x1 + x2 + x3) / 3
    y = (y1 + y2 + y3) / 3
    return x, y

def dovjina_vidrizka(x1, y1, x2, y2):
    довжина = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return довжина

def mediana(a, b, c):
    xA, yA = 0, 0
    xB, yB = a, 0
    xC, yC = (c ** 2 + b ** 2 - a ** 2) / (2 * c), ((c ** 2 - b ** 2 + a ** 2) * (b ** 2 - c ** 2 + a ** 2)) ** 0.5 / (2 * c)

    xM1, yM1 = tocka_pretinu(xB, yB, xC, yC, xA, yA)
    xM2, yM2 = tocka_pretinu(xA, yA, xC, yC, xB, yB)
    xM3, yM3 = tocka_pretinu(xA, yA, xB, yB, xC, yC)

    mediana1 = dovjina_vidrizka(xA, yA, xM1, yM1)
    mediana2 = dovjina_vidrizka(xB, yB, xM2, yM2)
    mediana3 = dovjina_vidrizka(xC, yC, xM3, yM3)

    return mediana1, mediana2, mediana3

# Введення довжин сторін трикутника
a = float(input("Введіть довжину сторони a: "))
b = float(input("Введіть довжину сторони b: "))
c = float(input("Введіть довжину сторони c: "))

# Обчислення медіан
медіани = mediana(a, b, c)
print("Довжина першої медіани: {:.2f}".format(медіани[0]))
print("Довжина другої медіани: {:.2f}".format(медіани[1]))
print("Довжина третьої медіани: {:.2f}".format(медіани[2]))