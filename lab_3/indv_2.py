import math

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

max_number = max(a, b, c)
sin_max = math.sin(max_number)

print("Синус максимального числа:", sin_max)
