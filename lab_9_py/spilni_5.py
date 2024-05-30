import os
import re

def sum_of_numbers_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Файл не знайдено. Будь ласка, переконайтесь, що шлях до файлу вказаний правильно.")
        return 0

    numbers = re.findall(r'\b\d+\b', text)

    total_sum = sum(map(int, numbers))

    return total_sum

path = os.path.dirname(os.path.realpath(__file__))
path = f"{path}/files/"

file_path = os.path.join(path, 't.txt') 

total_sum = sum_of_numbers_in_file(file_path)

print("Сума всіх чисел у файлі:", total_sum)
