#Ryan Meyer In Class Quiz Thursday, July 13th

#Make a TRUTH TABLE by hand for: not(a or b) and c
#a,b,c are booleans.

def truthtable (n):
    '''Truth table printed to lists. 0 = false, 1= true'''
    if n < 1:
        return [[]]
    subtable = truthtable(n-1)
    #print(subtable)
    return [ row + [v] for row in subtable for v in [0,1] ]

print(truthtable(3), "\nI'm not 100 percent sure this is what you are looking for, but not(a or b) and c can be found within this table")

# **************************************************
# Part 2
#
# Find the sum of ints from 50 to 250, INCLUSIVE
# that are not(even or divisible by 5) AND divisible by 3
# **************************************************
def sumNotEvenOrD5_butD3_ranged(num1, num2):
    '''prints out sum of ints within range (num1 to num2) that are NOT(even or divisible by 5) AND are divisible by 3'''
    goodNums = []
    summed = 0
    for i in range (num1, num2+1, 1):
        if (not(i%2 == 0 or i%5 == 0) and i%3 ==0):
            #goodNums.append(i)
            summed += i
            #print("{} is divisible by 3 but NOT even OR divisible by 5".format(i))
    return summed

print("Value of ints from 50 to 250 that are divisible by 3 but NOT even OR divisible by 5 is {}".format(sumNotEvenOrD5_butD3_ranged(50, 250)))
