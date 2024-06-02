# 2. Напишіть функцію для визначення, чи рік високосний, чи ні.


# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
    
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


year = int(input('Введите год: '))
ans = ['невисокосний', 'високосний']

# print(f"{year} рік високосний: {is_leap_year(year)}")
print(f"{year} рік {ans[is_leap_year(year)]}")