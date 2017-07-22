# Write the function FIND_HYPOT which, given the length of two sides of a right triangle
# returns the length of the hypotenuse.
# Ex: x ** .05 will return the square root
def find_hypot(s1,s2):
    '''given the length of two sides of a right triangle, returns the length of the hypotenuse'''
    hypotenuse = ((s1**2)+(s2**2))**(1/2)

    return hypotenuse

print("Hypotenuse of s1: {} and s2: {} is equal to {}".format(3,4,find_hypot(3,4)))
