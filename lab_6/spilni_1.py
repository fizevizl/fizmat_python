bullets = []

n = int(input("Введіть кількість оленів: "))
for i in range(n):
    k = int(input(f"Кількість кісточок для оленя {i+1} : "))
    bullets.append(k)

print(f"{sum(bullets)} нових саженців ")


