# У файлі regex_sum_1675329.txt (у прикріплених файлах) знайти кількість чисел та їх суму.

import re, os

def count_and_sum_numbers(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    

    numbers = re.findall(r'\b\d+\b', text)
    numbers = [int(num) for num in numbers]
    
    count = len(numbers)
    total_sum = sum(numbers)
    print(numbers)
    
    return count, total_sum

path = os.path.dirname(os.path.realpath(__file__))
file_path = f'{path}/regex_sum_1675329.txt'  

number_count, number_sum = count_and_sum_numbers(file_path)

print(f"Кількість чисел у файлі: {number_count}")
print(f"Сума чисел у файлі: {number_sum}")
