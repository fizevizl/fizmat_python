# У файлі regex_sum_1675329.txt (у прикріплених файлах) знайти кількість чисел та їх суму.

import re

def count_and_sum_numbers(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Файл не знайдено. Будь ласка, переконайтесь, що шлях до файлу вказаний правильно.")
        return 0, 0

    numbers = re.findall(r'\b\d+\b', text)
    
    numbers = [int(num) for num in numbers]
    
    count = len(numbers)
    total_sum = sum(numbers)
    
    return count, total_sum

file_path = 'C:/Git/fizmat_python/final_tasks/regex_sum_1675329.txt'  

number_count, number_sum = count_and_sum_numbers(file_path)

print(f"Кількість чисел у файлі: {number_count}")
print(f"Сума чисел у файлі: {number_sum}")
