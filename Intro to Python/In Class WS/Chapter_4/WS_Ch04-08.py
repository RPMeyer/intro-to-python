# **********************************************
# WS ch4_8
#
# Write a function, trngl_perim(x1,y1,x2,y2,x3,y3), which takes the
# coordinates of the 3 vertices of a triangle as parameters and
# which returns the perimeter of the triangle. Write a helper
# function, distance(x1,y1,x2,y2), which returns the distance
# between 2 points, which will be in the definition of
# trngl_perim(x1,y1,x2,y2,x3,y3). Check that both functions are
# working correctly.
#
# Find the perimeter of the triangle whose vertices are (1,2),(3,4),(5,6).
# ***********************************************
import math
def distance(x1, y1, x2, y2): #HELPER FUNCTION
    '''returns the distance between 2 points (x1, y1) (x2, y2)'''
    xDist = x2 - x1
    yDist = y2 - y1
    dist = math.sqrt(xDist**2 + yDist**2)
    return dist

def trngl_perim(x1, y1, x2, y2, x3, y3):
    '''takes the coordinates of the 3 vertices (points) of a triangle and which returns perimeter'''
    side1 = distance(x1, y1, x2, y2)
    side2 = distance(x2, y2, x3, y3)
    side3 = distance(x3, y3, x1, y1)

    perimeter = side1+side2+side3
    return perimeter

print(trngl_perim(1,2,3,4,5,6))
