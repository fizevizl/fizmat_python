# 3. Напишіть клас Coin, який описує монету, яку можна підкидати. 
# При створенні екземпляру класу, екземпляр отримує атрибут sideup зі значенням heads або tails.
# У класі визначте метод toss, який випадково визначає результат підкидання монети - орел чи решка.
# Створіть екземпляр класу і виведіть на екран n підкидань монети. Наприклад при n=3 можна отримати heads tails tails

import random

class Coin:
    def __init__(self):
        self.sideup = random.choice(["heads","tails"])

    def toss(self):
        self.sideup = random.choice(["heads","tails"])
        return self.sideup
    
c = Coin()
n = int(input("введіть число: "))

results = []
for i in range(n):
    results.append(c.toss())
print(results)