# **************************************************
# WS ch5_5
#
# Write a function, tell_if_d3_and_not_d5(num),
# which prints out an appropriate message for all num
# regarding if num is divisible by 3 but
# not divisible by 5.
#
# Use this function to print out an appropriate message
# for each int from 2 to 20.
# **************************************************
def tell_if_d3_and_not_d5(num):
    '''prints out appropriate message for all num regarding if num is divisible by 3 BUT NOT divisible by 5'''
    # Use this function to print out an appropriate message
    # for each int from 2 to 20.

    goodNums = []
    for i in range (num+1):
        if (i%3 == 0 and i%5 != 0):
            goodNums.append(i)
            print("{} is divisible by 3 but NOT 5".format(i))
    return goodNums

print(tell_if_d3_and_not_d5(50))
