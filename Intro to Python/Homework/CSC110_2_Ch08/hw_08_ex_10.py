# HW:10
#
# Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!):
# test(is_palindrome("abba"))
# test(not is_palindrome("abab"))
# test(is_palindrome("tenet"))
# test(not is_palindrome("banana"))
# test(is_palindrome("straw warts"))
# test(is_palindrome("a"))
# test(is_palindrome("")) # Is an empty string a palindrome?
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
    '''mirrors string argument'''
    return string[::-1]

def mirror(string):
    '''reverses string argument'''
    return string+string[::-1]

def is_palindrome(string):
    '''checks if (string) is palindrome'''
    if(reverse(string)==string):
        return True

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome("")) # Is an empty string a palindrome?
