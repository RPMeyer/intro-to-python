#Write a general program that asks for the STARTING day, amount of days, and returns the day of the week ended upon


def whichDay(startingDayInt, lengthInDays):
    '''asks for the STARTING day, amount of days, and returns the day of the week after amount'''
    listOfDays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

    if (lengthInDays > (7-startingDayInt)):
        lengthInDays = lengthInDays %7

    return listOfDays[startingDayInt+lengthInDays]

userDayStart = input("Enter current day of week - numerically. Ex: 4 ---> ")
userLength = input("Enter the amount of days to pass. Ex: 137 ---> ")
print(whichDay(0,137))
input("Press enter to close: ")
