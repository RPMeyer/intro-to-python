#Write a function proper_factors_of(n) which returns a list of proper factors of int (n) where n >=1.
# (n) is proper factor IF (F) DIVIDES (N) AND IF (f)<N
# NOTE: 1 HAS NO PROPER FACTORS

#--------------------------------------
def proper_factors_of(n):
    '''returns a list of proper factors of int (n) where n >=1.
    (n) is proper factor IF (F) DIVIDES (N) AND IF (f)< (n)'''
    factors =[]
    for i in range (1,n,1):
        if (n%i==0):
            factors.append(i)
    return factors

for n in [1,2,4,6]:
    pf = proper_factors_of(n)
    print('{0} has the proper factors {1}'.format(n,pf))

#--------------------------------------

# Write a function sum_of_proper_factors_of(n) which returns the sum of the proper factors of int n where n>=1.
#USE HELPER FUNCTION

def sum_of_proper_factors_of(n):
    '''returns the sum of the proper factors of int n where n>=1
    USES HELPER FUNCTION proper_factors_of(n)'''
    return sum(proper_factors_of(n))

for n in [1,2,4,6]:
    spf = sum_of_proper_factors_of(n)
    print('The sum of the proper factors of {0} is {1}.'.format(n,spf))

#--------------------------------------

# Write a function A_sequence(n) which returns a list containing a sequence of ints which start with int n, n>=1,
# in which the next term in the sequence is the sum of the proper factors of the previous term. Sequence stops if
#(1) if and when the sequence reaches 1, or
#(2) if and when a term occurs which appeared earlier in the sequence.
# USES PROPER FACTOR HELPER FUNCTIONS

def A_sequence(n):
    '''returns a list containing a sequence of ints which start with int n, n>=1
    USES PROPER FACTOR HELPER FUNCTIONS'''
    sumOfPrevious=[]
    previous=n
    for i in range(0,n):
        if previous not in sumOfPrevious and previous >= 1:
            sumOfPrevious.append(previous)
        previous = sum_of_proper_factors_of(previous)
    return sumOfPrevious

for n in range(1,13):
    A_seq = A_sequence(n)
    print('{0} has an A sequence of {1}'.format(n,A_seq))

#--------------------------------------

def longest_A_sequence(From, To):
    '''returns the longest A_sequence(n) (OR SEQUENCES~!) for 1<=From<=n<=135, together with the lengt of the sequence(s).'''
    longest=[]
    longestLen=0
    while (From>=1) and (From<=To):
        if len(longest)<= len(A_sequence(From)):
            longest.append(A_sequence(From))
        From+=1

    for i in range(0,len(longest),1):
        if longestLen<=len(longest[i]):
            longestLen=len(longest[i])
            
    print(len(longest[i]))
    return longest, longestLen
print(longest_A_sequence(1,135))
