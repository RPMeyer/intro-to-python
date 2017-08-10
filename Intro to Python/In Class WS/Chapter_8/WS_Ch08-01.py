# WS 8_1
#
# Write a function, numeric_value_ofL(Letter), which takes a single lower case
# or upper case letter & which returns 1 for an ‘a’ for an ‘A’, 2 for a ‘b’ or a ‘B’.
# …. 26 for a ‘z’ or a ‘Z’.
#-------------------------------------

def numeric_value_ofL(Letter):
    '''takes a single lower case or upper case letter & which
    returns 1 for an ‘a’ for an ‘A’, 2 for a ‘b’ or a ‘B’. …. 26 for a ‘z’ or a ‘Z’.'''
    alpha='abcdefghijklmnopqrstuvwxyz'
    Letter = Letter.casefold() #heck yah, thank you pyhton 3.3!!
    if len(Letter)==1:
        return alpha.find(Letter)+1
    else:
        return 'error'

print(numeric_value_ofL('S'))
