import turtle as t 

t.speed(20)
t.shape("triangle")
t.pensize(5)

# ==========================
#  variant 1
# ==========================
# t.color("green", "green")
# t.fd(90)
# t.rt(90)

# t.color("blue", "green")
# t.fd(90)
# t.rt(90)

# t.color("red", "green")
# t.fd(90)
# t.rt(90)

# t.color("yellow", "green")
# t.fd(90)
# t.rt(90)

# ==========================
#  variant 2 
# ==========================
# for color_pen in ["green", "blue", "red", "yellow"]:
#     t.color(color_pen, 'green')
#     t.fd(90)
#     t.rt(90)

# ==========================
#  variant 3
# ==========================
color_pen = ["green", "blue", "yellow", "red"]
for i in range(len(color_pen)):
    t.color(color_pen[i], 'green')
    t.fd(90)
    t.rt(90)

t.done()