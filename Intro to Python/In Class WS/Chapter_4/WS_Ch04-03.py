# *********************************************
# WS ch4_3
#
# Write a function, five_factorial(), which return 5! = 1*2*3*4*5
# ********************************************

def five_factorial():
    '''return 5! = 1*2*3*4*5'''
    prod_accum = 1
    for i in range(1,6,1):
        prod_accum *= i
    return prod_accum

print("Five! factorial is equal to {}".format(five_factorial()))
