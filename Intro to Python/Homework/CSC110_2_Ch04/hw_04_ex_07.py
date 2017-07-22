# Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to
# and including n. So sum_to(10) would be 1+2+3...+10 which would return the value
# 55.

def sum_to(n):
    '''returns the sum of all integer numbers up to and including n'''
    returnValue = 0
    for i in range(0,n+1,1):
        returnValue += i
        #print(returnValue) --testing summation
    return returnValue

print(sum_to(10)) #printing fruitful function
