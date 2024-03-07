N = int(input("Введіть початкову кількість волосся у діда Василя: "))

days = 0
hair_count = N

while hair_count > 0:
    days += 1
    hair_count *= 2

print(f"Дід Василь залишиться без волосся через {days} днів")
