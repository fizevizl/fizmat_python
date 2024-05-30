n = int(input("Введіть кількість сторінок книги "))
m = int(input("Введіть номер дня "))
for i in range(2,m+1):
    n=n-int(n/i)
print(f"Залишилось {n} сторінок")