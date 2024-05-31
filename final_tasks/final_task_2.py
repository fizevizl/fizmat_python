# 2. Напишіть функцію для визначення, чи рік високосний, чи ні.


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input('Введите год: '))

print(f"{year} рік високосний: {is_leap_year(year)}")