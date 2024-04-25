
# Вилосипедист-початківець Павлуша виїхав на широку дорогу. Але
# їхати інакше, ніж за законом синусоїди, йому ніяк не вдалося. Юний
# спортсмен стартував у точки x0 на вісі OX, а центри основ стовпців
# знаходяться у точках x1, x2, … , xn на цій же осі, яку перетинає
# синусоїда руху велосипедиста. Скільки стовпців може виявити на
# своєму шляху Павлуша, якщо шириною стовпа можна знехтувати?

import math

def count_columns(x0, xn, T):
    return math.floor((xn - x0) / T) + 1

x0 = float(input("Введіть координату початкової точки x0: "))
xn = float(input("Введіть координату кінцевої точки xn: "))
T = 2 * math.pi 

columns = count_columns(x0, xn, T)

print("Кількість стовпців, які виявить Павлуша:", columns)