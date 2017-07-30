# HW:1,2,3,4,7,16
# Youtube: 13
import sys

def test(did_pass):
    ''' print result of a test '''
    linenum = sys._getframe(1).f_lineno # get the callers line
    if(did_pass):
        msg = 'Test at line {} ok.'.format(linenum)
    else:
        msg = ('Test at line {} FAILED'.format(linenum))
    print(msg)

def test_suite():
    '''run the suite of test for code in this module (this file)'''
    test(abs(17) == 17)
    test(abs(-17) == 17)
    test(abs(0) == 0)
    test(abs(3.14) == 3.14)
    test(abs(-3.14) == 3.14)

test_suite()

def turn_clockwise(direction):
    ''' returns the next compass direction in a clockwise motion'''
    compassRose = {'n':'e','e':'s','s':'w','w':'n'}
    if direction in compassRose:
        return compassRose[direction][0]
    else:
        return None

test(turn_clockwise('n') == 'e')
test(turn_clockwise('w') =='n')
test(turn_clockwise('42') == None)
test(turn_clockwise('rubbish') == None)

def day_name(dayNum):
    '''returns the name of the day of week given the number. Assume 0 is sunday'''
    days={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    if dayNum in days:
        return days[dayNum]

test(day_name(3)=='Wednesday')
test(day_name(6)=='Saturday')
test(day_name(42)==None)

def day_num(dayName):
    ''' inverse of day_num() '''
    days={'Sunday':0,'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6}
    if dayName in days:
        return days[dayName]

test(day_num('Friday')==5)
test(day_num('Sunday')==0)
test(day_num(day_name(3))==3)
test(day_name(day_num('Thursday'))=='Thursday')

def day_add(dayName, delta):
    ''' returns the day of week after delta days have passed '''
    if (delta > (7-day_num(dayName))):
        delta = delta %7
    newDay = day_name((day_num(dayName))+delta)
    return newDay

test(day_add('Monday',4) == 'Friday')
test(day_add('Tuesday',14) == 'Tuesday')
test(day_add('Sunday',100) == 'Tuesday')

def to_secs(hours=0, minutes=0, seconds=0):
    ''' converts total hours, minutes, and seconds into total seconds'''
    minutes = minutes + (hours*60)
    seconds = seconds + (minutes*60)
    return seconds

test(to_secs(2,30,10) == 9010)
test(to_secs(2,0,0) == 7200)
test(to_secs(0,2,0) == 120)
test(to_secs(0,0,42) == 42)
test(to_secs(0,-10,10) == -590)

def is_factor(f, n):
    '''determines if (f) is a factor AKA DIVISIBLE (% 0) of (n)'''
    if (n%f == 0):
        return True
    else:
        return False

test(is_factor(3,12))
test(not is_factor(5,12))
test(is_factor(7,14))
test(not is_factor(7,15))
test(is_factor(1,15))
test(is_factor(15,15))
test(not is_factor(25,15))

#  YOUTUBE EXAMPLE 13 ------------------
#link: https://youtu.be/hDDt2KmNJ_s
def slope(x1, y1, x2, y2):
    '''returns the slope of the line through point(x1,y1) and point(x2,y2)'''
    m = (y2-y1)/(x2-x1) #formula for finding (m) the slope of a line between two points
    return m

test(slope(5,3,4,2)==1.0)
test(slope(1,2,3,2)==0.0)
test(slope(1,2,3,3)==0.5)
test(slope(2,4,1,2)==2.0)

def intercept(x1,y1,x2,y2):
    '''returns the y-intercept of line through point(x1,y1) and point(x2,y2)'''
    #uses slope() as helper function
    b = y1-(slope(x1,y1,x2,y2)*x1) #slope-point intercept formula, solving for (b), the y intercept, given point(x1,y1)
    return b
test(intercept(1,6,3,12)==3.0)
test(intercept(6,1,1,6)==7.0)
test(intercept(4,6,12,8)==5.0)
#-------------------------------
