def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

gcd_result = gcd(a, b)
lcm_result = lcm(a, b)

print("Найбільший спільний дільник (НСД):", gcd_result)
print("Найменший спільний кратний (НОК):", lcm_result)
