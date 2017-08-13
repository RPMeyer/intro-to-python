# HW:8,10
#
# Write a function that mirrors its argument:
# test(mirror("good") == "gooddoog")
# test(mirror("Python") == "PythonnohtyP")
# test(mirror("") == "")
# test(mirror("a") == "aa")

import sys

def test(did_pass):
    ''' print result of a test '''
    linenum = sys._getframe(1).f_lineno # get the callers line
    if(did_pass):
        msg = 'Test at line {} ok.'.format(linenum)
    else:
        msg = ('Test at line {} FAILED'.format(linenum))
    print(msg)

def mirror(string):
    '''mirrors string argument'''
    return string+string[::-1]

test(mirror("good") == "gooddoog")
test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")
