# Скласти програму яка обчислює площу прямокутної заготовки
# розміром a на b, якщо з неї вирізали чотири круга різного
# діаметру

import math

class Rectangle:
    def __init__(self, a, b, r1, r2, r3, r4):
        self.a = a
        self.b = b
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4

    @staticmethod
    def area_crcl(radius):
        return math.pi * radius ** 2

    def area(self):
        return self.a * self.b - self.area_crcl(self.r1) - self.area_crcl(self.r2) - self.area_crcl(self.r3) - self.area_crcl(self.r4)
    
    
rect = Rectangle(100, 100, 20, 20, 10, 10)

print(rect.area())


    
    
    
    


