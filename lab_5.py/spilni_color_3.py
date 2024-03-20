import turtle as t 

t.speed(100)
t.shape("circle")
t.pensize(2)

x = 0
y = 0
alpha = 360/8
t.goto(0,0)

for color_pen in ["green", "blue", "red", "yellow", "dark slate blue", "orange red", "dodger blue", "gray"]:
    t.color(color_pen, color_pen)
    r = 10

    
    for a in range(4):
        t.down
        r += 10
            
        for i in range(10):
            t.begin_fill()
            t.circle(r, 360)
            t.end_fill()
            t.fd(10)
            x = x + 10
        
       
        y = r*-0.5
        t.up()
        t.setpos(x,y)
        t.down()
        t.up()

        
     
            
    
    t.goto(0,0)
    t.rt(alpha)
    
t.done()