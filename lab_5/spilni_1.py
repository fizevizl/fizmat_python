import turtle as t 

t.speed(5)
t.reset
t.shape("turtle")
t.color("black", "green")
t.rt(190)
t.pensize(1)
for j in range(3):
    t.down()
    t.begin_fill()
    for i in range(4):
        t.fd(150)
        t.rt(90)
    t.rt(30)
t.done()