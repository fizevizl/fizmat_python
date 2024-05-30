x = int(input("Калорії в двох бутербродах "))
y = int(input("Калорії, які Іванка витрачає на спортивних секціях "))
y_new = y * 1.27

balance_before = 2 * x - y

balance_after = 2 * x - y_new

calories_difference = balance_before - balance_after

additional_sandwiches = calories_difference / x

print("Необхідно збільшити кількість бутербродів на", additional_sandwiches, "шт.")
