# *********************************************
# Ws ch3_5
# Initialize a sum accumulator to 0, then use a for loop & a range
# statement to add the ints from 1 to 10.
# ********************************************
sumAccum = 0;

for i in range(0,10+1,1):
    sumAccum += i
    #sumAccum = sumAccum + i;
print("The sum of integers from 1 to 10 is {}".format(sumAccum))
