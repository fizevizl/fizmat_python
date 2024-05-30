import os
import re
from collections import Counter

def most_common_words(file_path, n=5):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Файл не знайдено. Будь ласка, переконайтесь, що шлях до файлу вказаний правильно.")
        return []

    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    common_words = word_counts.most_common(n)
    return common_words

path = os.path.dirname(os.path.realpath(__file__))
path = f"{path}/files/"

file_path = os.path.join(path, 'text.txt')  

common_words = most_common_words(file_path)

print("П'ять найчастіше вживаних слів у файлі:")
for word, count in common_words:
    print(f"{word}: {count}")
