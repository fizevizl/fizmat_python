# 1. Дано натуральне ціле додатне число n. Визначити кількість цифр в ньому.

def count_simbol(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

n = int(input("введіть число: "))

print(f"Кількість цифр у числі:{count_simbol(n)}")
     