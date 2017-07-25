#*******************************
# ws ch7_1_
# Write a function, sum_of_odds(n). which returns
# the sum of the 1st n odd ints.
# Is there more than 1 way to do this?
#*******************************

def sum_of_odds(n):
    '''returns sum of the 1st n odd ints'''
    sumAccum=0
    for i in range(n):
        sumAccum += 2*i+1
    return sumAccum

print(sum_of_odds(5))
print(sum_of_odds(10))

#*******************************
# ws ch7_2
#
# Write a function, sum_of_odds_1(a,b),
# which returns the sum odd ints starting with
# the ath odd int & ending with the bth odd int.
# Use sum_of_odds(n) as a helper function.
# Is there more than one way to do this?
#*******************************
def sum_of_odds_1(a,b):
    '''returns the sum odd ints starting with the ath odd int & ending with the bth odd int'''
    #USE sum_of_odds(n) as HELPER FUNCTION
    return sum_of_odds(b)-sum_of_odds(a-1)

print(sum_of_odds_1(5,10))
