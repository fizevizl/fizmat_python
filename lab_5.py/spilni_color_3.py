import turtle as t 

t.speed(20)
t.shape("circle")
t.pensize(2)

alpha = 360/8
t.goto(0,0)

for color_pen in ["green", "blue", "red", "yellow", "dark slate blue", "orange red", "dodger blue", "gray"]:
    t.color(color_pen, color_pen)
    r = 10
    
    
    for i in range(10):
        t.down()
        t.begin_fill()
        t.circle(r, 360)
        t.end_fill()
        r += 10
        t.up()
        t.fd(20)
   
    t.goto(0,0)
    t.rt(alpha)
    
t.done()