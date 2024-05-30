# Створюємо словник з інформацією про пошукові системи
search_engines = {
    "Bing": 2.77,
    "Baidu": 1.42,
    "Ecosia": 0.13,
    "Yahoo": 1.31,
    "Yandex": 0.87,
    "Google": 92.47,
    "DuckDuckGo": 0.66,
    "Qwant": 0.02,
}

sorted_search_engines = dict(sorted(search_engines.items(), key=lambda item: item[1], reverse=True))

print("Перелік пошукових систем та відсоток їх використання за спаданням популярності:")
for engine, share in sorted_search_engines.items():
    print(f"{engine}: {share}%")
