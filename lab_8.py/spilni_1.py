# Знайти найменше спільне кратне чотирьох чисел створивши
# об’єкт з відповідним методом.

import math 

class Nsk:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find_nsk(self):
        return math.lcm(self.x, self.y)
 
a, b, c, d = (10, 4, 7, 9)

# variant 1
# obj = Nsk(a, b)
# res = obj.find_nsk()
# print(res)

# obj1 = Nsk(res, c)
# res = obj1.find_nsk()
# print(res)

# obj2 = Nsk(res, d)
# res = obj2.find_nsk()
# print(res)


# variant 2
print(Nsk(Nsk(Nsk(a, b).find_nsk(), c).find_nsk(), d).find_nsk())

