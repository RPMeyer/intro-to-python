# ----------------------------------------
# Ws ch9_1
#
# Write a function, Fibonacci(n), which returns a list of the first n terms of the
# Fibonacci series, n >= 2
# 1,1,2,3,5,8,13….
# ----------------------------------------
from math import sqrt

def fibonacchi(n):
    '''returns a list of the first (n) number terms of the fibonacchi series (ie: the sum of the 2 preceeding values adnaseum)'''
    a = 0
    b = 1
    counter = 0
    fibList = [a,b]
    while counter < n-2: #n-2 because the fibList already contains 2 values (0,1)
        a,b = b,a+b
        fibList.append(b)
        counter+=1
    return fibList

print(fibonacchi(10))
