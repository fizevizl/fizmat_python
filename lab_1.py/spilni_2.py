# Якщо на одну шальку терезів посадити Даринку, яка важить
# n кілограмів, і Наталку, яка важить на 5 кілограмів менше, а
# на іншу насипати m кілограмів цукерок, то скільки кілограмів
# цукерок доведеться з’їсти нещасним дівчаткам, щоб шальки
# терезів врівноважились?

n = float(input("Введіть вагу Даринки: "))
m = int(input("Введіть вагу цукерок: "))

weight_natalie = n - 5

sum = n + weight_natalie
j = sum - m 


print(f"Для вирівнювання шальок терезів, дівчатка повинні з'їсти {j} кг цукерок.")
