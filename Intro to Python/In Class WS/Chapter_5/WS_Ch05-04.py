# **************************************************
# WS ch5_4
#
# Find all ints from 2 to 250 that are divisible by 7 but not divisible by 3
# or by 5
# **************************************************

def good_ints():
    '''find all ints from 2 to 250 that are divisible by 7, but not by 3 OR 5'''
    goodNums = [] #EMPTY list
    for i in range(2,250+1,1):
        mod3 = i%3 == 0
        mod5 = i%5 == 0
        mod7 = i%7 == 0

        if (mod7 and not (mod3 or mod5)):
            goodNums.append(i) #append READ UP ON
    return goodNums

testingNums = good_ints()
print(good_ints())
