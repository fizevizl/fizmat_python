import math
a = 0.24
x = 9.86

b = (math.sin(x)+math.cos(3*x))**2 / math.log(2*(a+x)) - x**0.5
print(f"{b=}")