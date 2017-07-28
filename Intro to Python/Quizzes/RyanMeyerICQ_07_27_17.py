import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess draws POLYGONS using FOR LOOPS and FUNCTIONS")
t = turtle.Turtle() #CREATES THE TURTLE
t.color('blue')
t.pensize(3)
t.speed(0)

def poly_spiral(t,start_sz, del_sz, n_sides, max_length, color1, color2):
    '''uses turt to draw polygon with n sides and keeps drawing as long
    as the sum of the length changes by del_sz for the next side and continues as long as does not exceed max max_length.
    also prints number of sides drawn in the shell.
    USE A WHILE LOOP'''
    i=0
    counter = 0
    while i <= max_length:
        t.forward(start_sz)
        start_sz = start_sz + del_sz
        t.left(360/n_sides)
        i= abs(start_sz)
        if start_sz >0:
            t.color(color2)
        else:
            t.color(color1)

        counter+=1
    print("The number of sides drawn is: {}".format(counter))
#poly_spiral(t,5,1,8,50, 'red', 'blue')

poly_spiral(t,3,2,5,7500-1, 'red', 'blue')

#poly_spiral(t,200,-10,3, 200, 'red', 'blue')

t.exitonclick()
