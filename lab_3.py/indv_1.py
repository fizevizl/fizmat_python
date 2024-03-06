number = int(input("Введіть ціле число: "))

if number % 10 == 7:
    number *= 3
    print(f"Число було збільшено втричі:", number)
else:
    print("Число не закінчується цифрою 7.")
