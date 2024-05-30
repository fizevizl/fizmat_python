import turtle as t 

t.speed(100)
t.shape("circle")
t.pensize(15)

data = [(-150,0,"red",90), 
        (150,0,"green",110), 
        (0,-200,"purple",130)]

for x,y,z,d in data:
    t.up()
    t.setpos(x,y)
    t.down()

    for i in range(20):
        t.color(z)
        t.fd(d)
        t.goto(x,y)
        t.rt(20)

t.done()