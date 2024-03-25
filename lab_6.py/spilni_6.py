x = float(input("Введіть кількість мілілітрів на 1 коктейль (мл): "))
cost_500ml = float(input("Введіть вартість 0.5 літра інгредієнтів (грн): "))
cocktails = int(input("Введіть кількість коктейлів, яку плануєте приготувати: "))

total_ml = x * cocktails

total_cost = (total_ml / 1000) * (2 * cost_500ml)

print(f"Загальна вартість інгредієнтів: {total_cost} грн")
