# Дана не порожня послідовність слів, яка містить від 1-го до 8-ми літер; між сусідніми словами –
# кома, за останнім – крапка. Надрукувати всі слова, які відрізняються від останнього.

import os

path =  os.path.dirname(os.path.realpath(__file__))
path = f"{path}/files/"

with open(f"{path}text3.txt", "r", encoding="utf-8") as file_in:
    lines = file_in.readlines()

words = []
for line in lines:
    words += line.strip('.').split(',')

last_word = words[-1]

other_words = [word for word in words if word != last_word]

print(words)
print(last_word)
print(other_words)

