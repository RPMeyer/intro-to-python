# **********************************************
# WS ch4_9
#
# The number, e, Euler’s number, is an irrational number which has the value of
# 2.718281828459045 to that many decimals places. It is just as important as the
# number pi. [You can access the value of e from the math module as math.e.]
#
# A formula for ex is the infinite sum ex = 1 + x + x2/2! + x3/4! + …. + xn/n! + ….
#
#
# Write a function, e_to_the_x_series(x,n), which returns n terms of the above series:
# 1 + x + x2/2! + x3/4! + …. + xn/n!
#
# Use factorial(n) as a helper function in the definition of e_to_the_x_series(x,n).
#
# Print out a table of e^x for x from 0 to 5 in steps of .5. The table should have 3
# columns (don’t worry too much for now about making things line up):
# **********************************************
import math
def factorial(n): #HELPER FUNCTION
    '''returns n! and (n) is an int >= 1'''
    result = 1;
    for i in range(1, n+1, 1):
        result *= i
    return result

def e_to_the_x_series(x, n):
    '''returns n terms of the above series: 1 + x + x2/2! + x3/4! + …. + xn/n!'''
    sumAccum = 0
    for i in range(n): #(n) is the number of terms in series to be evaluated to
        sumAccum += (x**i)/factorial(i)

    return sumAccum

print("Computed value of e^x is: {}. Actual value of e^x is: {}".format(e_to_the_x_series(1,10), math.e))
