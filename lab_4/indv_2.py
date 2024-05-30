import math

N = int(input("Введіть ціле число N (> 1): "))
K = math.ceil(math.log(N, 5))

print(f"Найменше ціле число K, для якого 5^K > N: {K}")
