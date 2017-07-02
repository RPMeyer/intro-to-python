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
