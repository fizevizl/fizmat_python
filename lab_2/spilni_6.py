m = int(input("Введіть кількість хвилин, яку Олена Максимівна витрачає на перевірку домашніх завдань: "))
k = float(input("Введіть кількість разів, на які зросла кількість часу на перевірку через карантинні обмеження: "))

sleep_minutes = 7.5 * 60
household_minutes = 0.15 * 24 * 60
total_minutes = sleep_minutes + household_minutes
remaining_minutes = total_minutes - (m * k)

print("Олена Максимівна зможе присвятити прогулянці на свіжому повітрі", remaining_minutes, "хвилин.")
