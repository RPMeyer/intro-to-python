# HW:7,8,10
#
#Write a function that reverses its string argument, and satisfies these tests:
# test(reverse("happy") == "yppah")
# test(reverse("Python") == "nohtyP")
# test(reverse("") == "")
# test(reverse("a") == "a")
import sys

def test(did_pass):
    ''' print result of a test '''
    linenum = sys._getframe(1).f_lineno # get the callers line
    if(did_pass):
        msg = 'Test at line {} ok.'.format(linenum)
    else:
        msg = ('Test at line {} FAILED'.format(linenum))
    print(msg)

def reverse(string):
    '''reverses string argument'''
    return string[::-1]

test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")
