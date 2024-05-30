from math import ceil
k=int(input("ВВедіть кількість комп'ютерів в аудиторі?"))
kil=1
for days in range(14):
    kil = kil*2
aud = ceil(kil/k)   
print(f"Через два тижні без мотоциклів буде {kil} онуків")
print(f"В закладі освіти повинно бути {aud} компютерних аудиторій")