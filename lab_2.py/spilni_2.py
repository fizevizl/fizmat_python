m,n = map(float, input("Введіть розмір полотна у метрах ").split())
s = float(input("Введіть вартість фарби за 100 мл "))
Square = m*n*10000
Color = Square*2
Money = Color/100*s
print( 'Для картини необхідно залучити {:.3f} гривень'.format(Money) )