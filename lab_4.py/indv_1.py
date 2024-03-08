a = int(input("Введіть ціле число a (0 ≤ a ≤ 50): "))

if a < 0:
    a = 0
elif a > 50:
    a = 50

sum_of_squares = 0

for i in range(a, 51):
    sum_of_squares += i ** 2

print(f"Сума квадратів всіх цілих чисел від {a} до 50: {sum_of_squares}")
