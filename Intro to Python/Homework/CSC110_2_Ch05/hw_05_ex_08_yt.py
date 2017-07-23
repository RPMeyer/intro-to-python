# Modify the turtle bar chart program so that the bar for any value of
# 200 or more is filled with red,
# values between [100 and 200) are filled with yellow and
# bars representing values less than 100 are filled with green

#YOUTUBE VIDEO LINK: https://youtu.be/mQFCJ5g5e4Y


import turtle
tess = turtle.Turtle() #Create tess and set some attributes

#Set up the window and its attributes
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess.speed(0)
tess.color("blue", "red")
tess.pensize(3)

def draw_bar(t, height):
    '''Get turtle t to draw one bar, of height.'''
    t.begin_fill()
    if (height >= 200): #200 or more is filled with red
        t.fillcolor("red")
    elif (height >= 100 and height < 200): #values between [100 and 200) are filled with yellow
        t.fillcolor("yellow")
    elif (height <100): #values less than 100 are filled with green
        t.fillcolor("green")
    t.left(90)
    t.forward(height)
    t.write(" "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)


xs = [48,117,200,240,160,260,220]
for a in xs:
    draw_bar(tess, a)

wn.mainloop() #leaves turtle program openm rather than simply closing upon execution
