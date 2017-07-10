# ***********************************************
# WS ch4_4
#
# Write a function, factorial(n), which returns n! . n is an int >=1.
# ***********************************************
def factorial(n):
    '''returns n! and (n) is an int >= 1'''
    result = 1;
    for i in range(1, n+1, 1):
        result *= i
    return result

n = 10 #hardcoded value to compute factorial
userValue = int (input("Please enter the integer to be used: "))
print("The value of {}! factorial is equal to: {}".format(userValue, factorial(userValue)))

input("press enter to close: ") #forces to the script to hold until complete - preventing the cmd from closing
