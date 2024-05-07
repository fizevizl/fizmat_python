# Знайти найменше спільне кратне чотирьох чисел створивши
# об’єкт з відповідним методом.

import math 

class Nsk:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find_nsk(self):
        return math.lcm(self.x, self.y)
 
a, b, c, d = (11, 22, 33, 44)

obj = Nsk(a, b)
res = obj.find_nsk()

obj1 = Nsk(res, c)
res = obj1.find_nsk()

obj2 = Nsk(res, d)
res = obj2.find_nsk()
print(f"variant 1: {res}")

res = Nsk(Nsk(Nsk(a, b).find_nsk(), c).find_nsk(), d).find_nsk()
print(f"variant 2: {res}")

