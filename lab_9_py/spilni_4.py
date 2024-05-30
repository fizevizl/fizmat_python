import re
import os

path =  os.path.dirname(os.path.realpath(__file__))
path = f"{path}/files/"


def get_unique_words(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Файл не знайдено. Будь ласка, переконайтесь, що шлях до файлу вказаний правильно.")
        return []

    words = re.findall(r'\b\w+\b', text.lower())

    unique_words = set(words)
    
    return sorted(unique_words)

unique_words = get_unique_words(path)

print("Список унікальних слів:")
for word in unique_words:
    print(word)
