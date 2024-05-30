import math
x = int(input("Введіть кількість куплетів по 4 "))
z = int(input("Введіть кількість куплетів по 6 "))
V = 4
S1 = x*4
S2 = z*6
t1 = S1/V
t2 = S2/V
print( 'Забудькуватість коштує {:d} хвилин(у/и)'.format(math.ceil(abs(t1-t2))) )