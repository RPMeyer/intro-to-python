# ----------------------------------------
# WS ch 9_2
#
# Of the first 40 Fibonacci numbers, which of these are prime numbers?
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

def checkPrime(n):
    '''if (n) is prime, returns true'''
    if (n==2) or (n==3):
        return True
    if (n%2==0) or (n<2):
        return False

    for i in range(3,int(n**0.5)+1,2):# only odd numbers because even numbers are NOT PRIME
        if (n%i==0):
            return False
    return True
n=10
fibonacchiList = fibonacchi(n)
for i in fibonacchi(n):
    if (checkPrime(i)==True):
        print('Of the first {} values in the fibonacci series, {} is a prime.'.format(n,i))
