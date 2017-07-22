# # IN CLASS INTRO TO FUNCTIONS
# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# wn.title("Alex draws a square")
# alex = turtle.Turtle() #CREATES THE TURTLE
#
# def square_1(t, Size):
#     '''Draws a square of size Size using turtle t'''
#     for i in range(4):
#         t.forward(Size)
#         t.left(90)
#
# # square_1(alex, 100)
# # square_1(alex, 200)
# # square_1(alex, 300)
#
#
# # ---------------------------------
# # new FUNCTION called pinwheel
# # THIS IS GREAT. SOAK THIS ONE UP. RETAIN IT. THIS IS IMPORTANT. FUNCTIONS. FUNCTIONS IN FUNCTIONS. TRULY UNDERSTAND IT. LEARN!
# def pinwheel(t,Size):
#     '''Draws a square of size Size followed by a rotation left of 30 degrees. Runs 12 times.'''
#     for i in range(0,12+1,1):
#         square_1(t,Size)
#         t.lt(30)
#
# pinwheel(alex, 100)

import math
# Write a function, circle_area(Radius),which
# returns the area of a circle of radius Radius.
# Then use the function to print out a table of
# radii and corresponding circle areas for the
# radii 1,3,7,10. Round the circle areas to 3
# decimal points.
def circle_area(Radius):
    '''returns area of circle (Radius) radius'''
    area = math.pi * Radius
    return area

# print(circle_area(10))

def circle_area_table(radii):
    print('Radius   Area')
    print('-------------')
    # radii = [1,3,7,10]
    for i in radii:
        print(i, '| ',circle_area(i))

circle_area_table([1,3,7,10])
