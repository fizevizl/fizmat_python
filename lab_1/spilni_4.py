from math import sqrt

R = float(input('Введіть радіус капелюха '))
l = R * sqrt(2)
print(f'Потрібна коробка розміром {l:6.4} на {l:6.4}')