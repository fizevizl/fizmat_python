total_time = 120

x = int(input("введіть час :"))
y = int(input("введіть час :"))
z = int(input("введіть час :"))

translation_time = total_time - x - y - z
word_translation_time = 5

translated_words = translation_time // word_translation_time

print(f"Сашко встиг перекласти {translated_words} слів.")
