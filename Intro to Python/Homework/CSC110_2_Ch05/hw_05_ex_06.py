# Write a function that is given an exam percentage and
# returns the grade FIRST, UPPER SECOND, SECOND, THIRD, F1 SUPP, F2, F3

listOfGrades = ['FIRST', 'UPPER SECOND', 'SECOND', 'THIRD', 'F1 SUPP', 'F2', 'F3']
listOfScores = [83,75,74.9,70,69.9,65,60,59.9,55,50,49.9,45,44.9,40,39.9,2,0]

def getGrade(score):
    grades = {'First':(75,101),'Upper Second':(70,74),'Second':(60,69),'Third':(50,59),'F1 Supp':(45,49),'F2':(40,44),'F3':(0,39)}
    score = int(score)
    for grade in grades:
        if (grades[grade][0] <= score and score <= grades[grade][1]):
            return grade

for i in listOfScores:
    print(getGrade(i))
