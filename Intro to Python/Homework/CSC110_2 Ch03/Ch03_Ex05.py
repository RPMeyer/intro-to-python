# Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# (a) Write a loop that prints each of the numbers on a new line.
# (b) Write a loop that prints each number and its square on a new line.
# (c) Write a loop that adds all the numbers from the list into a variable called total.
#   You should set the total variable to have the value 0 before you start adding them up,
#   and print the value in total after the loop has completed.
# (d) Print the product of all the numbers in the list. (product means all multiplied together)

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# (a) Write a loop that prints each of the numbers on a new line.
for i in xs:
    print("{}".format(i))

# (b) Write a loop that prints each number and its square on a new line.
for i in xs:
    iSquared = i**2
    print("{} and its square is: {}".format(i,iSquared))

# (c) Write a loop that adds all the numbers from the list into a variable called total.
#   You should set the total variable to have the value 0 before you start adding them up,
#   and print the value in total after the loop has completed.
xsTotal = 0
for i in xs:
    print("The current sum of the list, {}, plus the next int, {}, is {}".format(xsTotal, i, xsTotal +i))
    xsTotal = xsTotal + i
print("The sum of integers in the list xs is {}".format(xsTotal))

# (d) Print the product of all the numbers in the list. (product means all multiplied together)
xsProducts = xs[0]
for i in xs[1:]:
    xsProducts = xsProducts * i;
    print("{}".format(xsProducts))
print("The product of every integer in the list 'xs' is {}".format(xsProducts))
