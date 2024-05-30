
def nds(a, b):
    while b:
        a, b = b, a % b
    return a

def sho(a, b):
    return a * b // nds(a, b)

def ono(a, b, c, d):
    gcd_ab = nds(a, b)
    gcd_cd = nds(c, d)
    gcd_abcd = nds(gcd_ab, gcd_cd)
    return (a * b * c * d) // gcd_abcd

a = input("введіть 1ше число: ")
b = input("введіть 2ге число: ")
c = input("введіть 3те число: ")
d = input("введіть 4те число: ")

lcm_four = ono(a, b, c, d)

print("Найменше спільне кратне чотирьох чисел:", lcm_four)
