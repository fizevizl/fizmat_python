import math

m = float(input("Введіть довжину листа : "))
n = float(input("Введіть ширину листа : "))
p = float(input("Введіть товщину листа : "))
r1 = float(input("Введіть радіус 1 отвору : "))
r2 = float(input("Введіть радіус 2 отвору : "))
r3 = float(input("Введіть радіус 3 отвору : "))
r4 = float(input("Введіть радіус циліндра : "))
h = float(input("Введіть висоту циліндра : "))

V1 = math.pi * r1**2
V2 = math.pi * r2**2
V3 = math.pi * r3**2

V_cylinder = math.pi * r4**2 * h
V_list = m * n * p
V_ostatok = V_list - (V1 + V2 + V3)

if V_ostatok >= V_cylinder:
    print("Кількість свинцю, що залишилась, достатня для витискання циліндра.")
else:
    print("Кількість свинцю, що залишилась, недостатня для витискання циліндра.")
