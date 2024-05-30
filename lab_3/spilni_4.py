import datetime # Модуль для роботи з датами
x = datetime.datetime.now() # Поточна дата

d,m,y = map(int, input("Введіть ваш день народження (ДД-ММ-РРРР)").split("-"))

if x.month>m: # якщо його день народження був у пройденому місяці
    full_year = x.year-y
elif x.month==m and x.day>=d: # якщо його день народження у цьому місяці, але ще не відбувся
    full_year = x.year-y
else:
    full_year = x.year-y-1 # якщо його день народження буде в наступних днях місяця
# print(full_year)

if full_year<6:
    print("вибач, малюк")    
elif (full_year>=6 and full_year<=12) or full_year>=66:
    print("базові знання")
elif full_year<=17:
    print("розширені знання")
elif full_year<=25:
    print("сучасні тренди")
else:
    print("енцеклопедичні відомості")