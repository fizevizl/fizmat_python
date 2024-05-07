# Скласти програму яка підраховує кількість слів в текстовому файлі довжина
# яких дорівнює числу 5.

import os

path =  os.path.dirname(os.path.realpath(__file__))
path = f"{path}/files/"

with open(f"{path}text.txt", "r", encoding="utf-8") as file_in:
    lines = file_in.readlines()

words_equals_5 = 0
words = []

for line in lines:
    tmp = line.strip().split()
    words += tmp

for word in words:
    if len(word) == 5:
        words_equals_5 += 1
        print(word)
        
print("count =",words_equals_5)

 
