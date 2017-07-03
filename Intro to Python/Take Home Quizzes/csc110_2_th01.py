userName = input("What is your name: ");
boxLength = int(input("What is the length of the box: "));
boxWidth = int(input("What is the width of the box: "));
boxHeight = int(input("What is the height of the box: "));
userUnits = input("What unit standards are the box measurements in: ");

boxVolume = boxLength*boxWidth*boxHeight;
boxSurfaceArea = 2*(boxWidth*boxHeight) + 2*(boxWidth*boxLength) + 2*(boxLength*boxHeight);

print("""The box volume is {} {}**3""".format(boxVolume, userUnits));
print("""The box surface area is {} {}**2""".format(boxSurfaceArea, userUnits));
print("press ENTER to close:");
