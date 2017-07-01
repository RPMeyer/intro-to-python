# 1. Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable,
#   then print out the sentence on one line using print.

allAll = "All";
workWork = "work";
andAnd = "and";
noNo = "no";
playPlay = "play";
makesMakes = "makes";
jackJack = "jack";
aA = "a";
dullDull = "dull";
boyBoy = "boy";
periodPeriod = ".";
print(allAll, " " + workWork, " " + andAnd, " " + noNo, " " + playPlay, " " + makesMakes, " " + jackJack, " " + aA, " " + dullDull, " " + boyBoy + periodPeriod);

# 3. Place a comment before a line of code that previously worked, and record what happens when you rerun the program.
#just nother comment going here
print(allAll, " " + workWork, " " + andAnd, " " + noNo, " " + playPlay, " " + makesMakes, " " + jackJack, " " + aA, " " + dullDull, " " + boyBoy + periodPeriod);

# 4. Start the Python interpreter and enter bruce + 4 at the prompt. This will give you an error:
#   NameError: name ’bruce’ is not defined
#   Assign a value to bruce so that bruce + 4 evaluates to 10
bruce = 6;
print(bruce+4);
# 5. The formula for computing the final amount if one is earning compound interest is given on Wikipedia as LOOK IN BOOK FOR IMAGE
#   Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8%.
#   Then have the program prompt the user for the number of years t that the money will be compounded for. Calculate and
#   print the final amount after t years

# 6. Evaluate the following numerical expressions in your head, then use the Python interpreter to check your results:
# (a) >>> 5 % 2 = 1
# (b) >>> 9 % 5 = 4
# (c) >>> 15 % 12 = 3
# (d) >>> 12 % 15 = 12
# (e) >>> 6 % 6 = 0
# (f) >>> 0 % 7 = 0
# (g) >>> 7 % 0 = 0
print(5%2, 9%5, 15%12, 12%15, 6%6, 0%7)
print(9%5)
print(15%12)
print(12%15)
print(6%6)
print(0%7)
# print(7%0) ERROR INTEGER DIVISION BY ZERO

# What happened with the last example? Why? If you were able to correctly anticipate the computer’s response in all but the last one, it is time to move on.
#   If not, take time now to make up examples of your own. Explore the modulus operator until you are confident
#   you understand how it works.

# 7. You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off?
#   (Hint: you could count on your fingers, but this is not
#   what we’re after. If you are tempted to count on your fingers, change the 51 to 5100.)
# THE SOLUTION SHOULD BE 5AM (WO DAYS LATER)
currentTime = 2;
pmOrAm = "pm"; #pm
pmOrAm2 = "pm"; #pm
alarmInHours = 51;

for x in range(0, 51, 12):
    if pmOrAm == "pm":
        pmOrAm = "am"
    else: pmOrAm = "pm";

timeForAlarm = str(currentTime + (51%12)) + pmOrAm;
print("The time when the alarm goes off will be: ", timeForAlarm)
# PASSED INTO PRINT USING NEW FORMATTING -- I like this. This is good.
print("The time the alarm goes off will be {}".format(timeForAlarm));


#-----Testing with user input for alarm length/time------
alarmUserDefined = int(input("Using integers, set the number of hours until alarm: " ));
for x in range(0, alarmUserDefined, 12):
    if pmOrAm2 == "pm":
        pmOrAm2 = "am"
    else: pmOrAm2 = "pm";
timeForUserAlarm = str(currentTime + (alarmUserDefined%12)) + pmOrAm2;
print("The time the USERS alarm goes off will be {}".format(timeForUserAlarm));
#-----DONE TESTING-----
