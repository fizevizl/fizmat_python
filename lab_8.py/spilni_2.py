# Дано a,b,c – довжини сторін трикутника. Знайти медіани
# трикутника, сторонами якого є медіани даного трикутника,
# створивши об’єкт трикутник


class Triangle:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def medians(self):
        ma = (self.c**2 + self.b**2 - self.a**2) ** 0.5 / 2
        mb = (self.a**2 + self.c**2 - self.b**2) ** 0.5 / 2
        mc = (self.a**2 + self.b**2 - self.c**2) ** 0.5 / 2
        return (ma, mb, mc)


tr_big = Triangle(10, 10, 10)
medians_tr_big = tr_big.medians()
tr_small = Triangle(*medians_tr_big)
print(tr_small.medians())         
