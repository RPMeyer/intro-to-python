#hw 1,2,6,10,12 YT 8
# Assume the days of the week are numbered 0,1,2,3,4,5,6 from SUNDAY to SATURDAY.
# Write a function which is given the day number and RETURNS the day name - a STRING


def dayOfWeek(dayNumber):
    '''Given (n) numbered day of week, returns string of corresponding day'''
    listOfDays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

    return listOfDays[dayNumber]

print(dayOfWeek(5))
