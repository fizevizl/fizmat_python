from turtle import *

for j in range(8):
 up()
 goto(0, 0)
 rt(45)
 col = ["black", "magenta", "purple", "blue", "green", "yellow", "orange", "red"]
 color(col[j])
 down()
 pensize(1)
 fd(30)
 for i in range(5):
  pensize(15 * (i + 1))
  fd(30)

exitonclick()
mainloop()