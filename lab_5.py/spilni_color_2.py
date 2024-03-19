import turtle as t 

t.speed(20)
t.shape("circle")
t.pensize(5)

alpha = 360/7

for color_pen in ["green", "blue", "red", "yellow", "dark slate blue", "orange red", "dodger blue"]:
    t.color(color_pen, 'green')
    t.circle(150, 360)
    t.rt(alpha)

t.done()