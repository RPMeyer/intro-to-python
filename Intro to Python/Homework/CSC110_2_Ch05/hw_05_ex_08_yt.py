# Modify the turtle bar chart program so that the bar for any value of
# 200 or more is filled with red,
# values between [100 and 200) are filled with yellow and
# bars representing values less than 100 are filled with green

def draw_bar(t, height): 2 3 4 5 6
""" Get turtle t to draw one bar, of height. """ # Added this line
t.begin_fill() t.left(90)
t.forward(height)
t.write(" "+ str(height))
t.right(90) t.forward(40) t.right(90)
t.forward(height) t.left(90)
t.end_fill() t.forward(10)
wn = turtle.Screen() wn.bgcolor("lightgreen")
tess = turtle.Turtle() tess.color("blue", "red") tess.pensize(3)
# Create tess and set some attributes # Added this line # Set up the window and its attributes
xs = [48,117,200,240,160,260,220] for a in xs: draw_bar(tess, a)
wn.mainloop()
