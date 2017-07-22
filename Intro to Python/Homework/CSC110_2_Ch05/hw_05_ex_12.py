# Write a function is_rightAngled which given the length of
# three sides will determine if the triangle is right angled.
# It will return true or false - the sides can be given to the function in any order

def find_hypot(side1,side2):
    '''given the length of two sides of a right triangle, returns the length of the hypotenuse'''
    hypotenuse = ((side1**2)+(side2**2))**(1/2)

    return hypotenuse

def is_rightAngled(side1, side2, side3):
    '''length of three sides will determine if the triangle is right angled.
    It will return true or false - the sides can be given to the function in any order'''
    if side3 == find_hypot(side1,side2):
        return True
    return False

print(is_rightAngled(2.5,10.5,10.793516572461451))
