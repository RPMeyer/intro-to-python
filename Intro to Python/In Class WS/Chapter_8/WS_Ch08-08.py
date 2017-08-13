# Ws ch8_8
#
# Redo the 15 primes per line table for primes <= 1000 using the string
# format method.
#-------------------------------------
def isPrime(n):
    '''if (n) is prime, returns true'''
    if (n==2) or (n==3):
        return True
    if (n%2==0) or (n<2):
        return False

    for i in range(3,int(n**0.5)+1,2):# only odd numbers because even numbers are NOT PRIME
        if (n%i==0):
            return False
    return True

def primeTablePrinter(lineLength=15, n=1000):
    '''prints a table of lines with each line being lineLength in length'''
    counter=0
    primeCounter=0
    while (counter <=n):
        if (isPrime(counter)==True):
            primeCounter+=1
            print ('{0:{width}}'.format(counter,width=5),end='')
            if(primeCounter%lineLength==0):
                print()
        counter+=1

primeTablePrinter()
