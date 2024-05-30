from math import pi
d = float(input("Введіть діаметр плями (розмір пенька)"))
S_pl = pi*d*d/4
s = float(input("Введіть максимальний розмір, що може почистити хімчистка "))
m = float(input("Введіть вартість послуги хімчистки "))
n = float(input("Введіть вартість нових штанів "))
if S_pl > s:
    vart_min = n
else:
    vart_min = m
if vart_min < n:
    print(vart_min)
else:
    print(n)