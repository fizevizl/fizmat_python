import turtle as t 

t.speed(5)
t.reset
t.shape("turtle")
t.color("black", "green")
t.pensize(3)
n = 20
delta = 20
for a in range(10):
    for b in range(2):
        t.fd(n)
        t.rt(-90)
        n += delta
t.done()