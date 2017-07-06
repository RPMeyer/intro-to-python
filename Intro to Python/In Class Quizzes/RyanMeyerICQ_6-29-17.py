##In class quiz from thursday, June 29th, 2017

##1 [10 pts] Use a loop with a RANGE STATEMENT AND A SUM ACCUMULATOR to find:
##(A) The SUM of reciprocal EVEN INTS from 6 to 22 (USE ROUND FUNCTION TO 4 DEMICAL PLACES)
##(B) The SUM of ODD INT reciprocal square roots from 9 to 31 (USE ROUND FUNCTION TO 4 DEMICAL PLACES)
##(C) Add the computed SUMS from A AND B together (USE ROUND FUNCTION TO 4 DEMICAL PLACES)

sumEvenRecip = 0;
sumOddRecipSquared = 0;
sumOfSums = 0;

##(A) The SUM of reciprocal EVEN INTS from 6 to 22 (USE ROUND FUNCTION TO 4 DEMICAL PLACES)
for x in range(6,22+1,2):
    sumEvenRecip = sumEvenRecip + 1/x;
print("Sum A is ", round(sumEvenRecip,4)); ##ANSWER

##(B) The SUM of ODD INT reciprocal square roots from 9 to 31 (USE ROUND FUNCTION TO 4 DEMICAL PLACES)
for x in range(9,31+1,2):
    sumOddRecipSquared = sumOddRecipSquared + 1/(x**2);
print("Sum B is ", round(sumOddRecipSquared,4)); ##ANSWER

##(C) Add the computed SUMS from A AND B together (USE ROUND FUNCTION TO 4 DEMICAL PLACES)
sumOfSums = sumEvenRecip + sumOddRecipSquared;
print("Sum C is ", round(sumOfSums, 4)); ##ANSWER
