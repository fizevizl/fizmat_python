import math
xa,ya = map(float, input('Введіть координати точки А ').split() )
xb,yb = map(float, input('Введіть координати точки B ').split() )
xc,yc = map(float, input('Введіть координати точки C ').split() )
ab=math.sqrt((xa-xb)**2+(ya-yb)**2)
bc=math.sqrt((xc-xb)**2+(yc-yb)**2)
ac=math.sqrt((xa-xc)**2+(ya-yc)**2)
p=(ab+bc+ac)/2
S=math.sqrt(p*(p-ab)*(p-bc)*(p-ac))
print('S = {:.2f}'.format(S))