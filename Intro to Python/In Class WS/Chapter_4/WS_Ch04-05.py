# *************************************************
# WS ch 4_5
#
# Use factorial(n) to print out a table of n! for 1 <= n <= 10.
# ************************************************

def factorial(n):
    '''returns n! and (n) is an int >= 1'''
    result = 1;
    for i in range(1, n+1, 1):
        result *= i
    return result

factorialList = []
factorialInitials = []

for i in range(1, 10+1, 1):
    factorialInitials.append(i)
    factorialList.append(factorial(i))

zippedList = list(zip(factorialInitials, factorialList))
print('\n'.join(map(str, factorialList)))

headers = ["name","level","value"]

max_lens = [len(str(max(i, key=lambda x: len(str(x))))) for i in zip(headers, factorialInitials, factorialList)]

for row in (headers, factorialInitials, factorialList):
    print ('|'.join('{0:{width}}'.format(x, width=y) for x, y in zip(row, max_lens)))


#print(factorialList, factorialInitials)



# *************************************************
# WS ch 4_5A
#
# Write a function, f2c(fahr), that takes degrees in Fahrenheit &
# returns Celsius degrees.
# Write a function, f2k(fahr), that takes Fahrenheit degrees & returns
# Kelvin degrees. Use f2c(fahr) as a helper function.
# 32F ~ 0C, 212F ~ 100C
# deg K = deg C + 273.15
# ************************************************

def f2c(fahr):
    '''takes degrees in Fahrenheit and returns Celsius degrees''' #will be used as a HELPER FUNCTION
    celsius = (fahr - 32)/1.8
    return celsius

def f2k(fahr):
    '''takes Fahrenheit degrees & returns Kelvin degrees'''
    kelvin = f2c(fahr) + 273.15
    return kelvin

print(f2k(70)) #testing conversion -- result A-OK
