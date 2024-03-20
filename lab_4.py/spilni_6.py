N=int(input("Скільки раундів продовжувалась гра?"))
dVas=3
dGor=5
Vas=0
Gor=0
for _ in range(N):
    Vas = Vas + dVas
    dVas = dVas + 3
    Gor = Gor + dGor
    dGor = dGor + 5
print(f"Безпосередньо Горинич з'їв {Gor} шашок")
print(f"Враховуючи з'їдені Василиною - {Gor+Vas} шашок")