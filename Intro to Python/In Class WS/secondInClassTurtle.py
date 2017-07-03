# Second turtle
# WS3-2

import turtle
wn = turtle.Screen()
bg_clr = input('Enter a bg color: ')
wn.bgcolor(bg_clr)

wn.title("Hello, Tess!")

tess = turtle.Turtle()
tess_color = input('Enter a tess line color: ')
tess.color(tess_color)

tessPenSize = int(input('Enter a pen size for Tess: '))
tess.pensize(tessPenSize)

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop();
