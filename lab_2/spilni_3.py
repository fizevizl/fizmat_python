from math import ceil
n = int(input("Введіть кількість яєць за день "))
print( 'Потрібно {:d} коробок'.format(ceil(n*7/200)) )