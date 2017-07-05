# ************************************************
# WS ch 3_6
# Initialize a product accumulator to 1, then use a for loop & a range
# statement to multiply the ints from 1 to 5.
# ************************************************
prodAccum = 1;

for i in range(1, 5+1, 1):
    prodAccum *= i
print("The product of the integers from 1 to 5 is {}".format(prodAccum))
