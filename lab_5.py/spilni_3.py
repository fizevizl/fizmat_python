import turtle as t 

t.speed(20)
t.shape("turtle")
t.color("black", "green")
t.pensize(2)
t.rt(24)
r = 10
for i in range(10):
    t.down()
    t.circle(r, 360)
    r += 10
    t.up()
    t.fd(20)
t.done()