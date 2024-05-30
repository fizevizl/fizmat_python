# Створити клас Гроші для роботи з грошовими сумами. Число
# повинно бути представлено двома полями: для гривень і
# двозначне для копійок. Дрібна частина (копійки) при виведенні
# на екран повинна бути відокремлена від цілої частини коми.
# Реалізувати додавання, віднімання, додавання одним числом,
# множення на дробове число


class Money:
    def __init__(self, grn, kop) -> None:
        self.grn = grn
        self.kop = kop

    def __str__(self):
        return f"{self.grn},{self.kop:02d}"

    def __add__(self,other):
        total_kop = self.kop + other.kop
        over_money = total_kop // 100
        total_kop %= 100
        total_grn = self.grn + other.grn + over_money
        return Money(total_grn, total_kop)

    def __sub__(self, other):
        total_kop_self = self.grn * 100 + self.kop
        total_kop_other = other.grn * 100 + other.kop
        total_kop = total_kop_self - total_kop_other

        total_grn = total_kop // 100
        total_kop %= 100
        return Money(total_grn, total_kop)
    
    def __mul__(self, other):
        total_kopiyka = int((self.grn * 100 + self.kop) * other)
        total_hryvnia = total_kopiyka // 100
        total_kopiyka %= 100
        return Money(total_hryvnia, total_kopiyka)

        
m1 = Money(15, 90)
m2 = Money(0, 15)

result = m1 + m2
print("Додавання:", result)

result = m1 - m2
print("Віднімання:", result)

result = m1 * 1.7
print("Множення на дробове число:", result)

