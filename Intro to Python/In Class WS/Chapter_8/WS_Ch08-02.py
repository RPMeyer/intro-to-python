# WS 8_2
#
# Write a function, numeric_value_ofW(Word), which takes a Word, a
# combination of only lower case and upper case letters, and which uses
# numeric_value_of(Letter) tor return the value of the word as the sum of the
# values of the letters in Word.
#-------------------------------------

def numeric_value_ofL(Letter):
    '''takes a single lower case or upper case letter & which
    returns 1 for an ‘a’ for an ‘A’, 2 for a ‘b’ or a ‘B’. …. 26 for a ‘z’ or a ‘Z’.'''
    alpha='abcdefghijklmnopqrstuvwxyz'
    Letter = Letter.casefold() #heck yah, thank you pyhton 3.3!!
    for i in Letter:
        return alpha.find(i)+1
    else:
        return 'error'

def numeric_value_ofW(Word):
    '''takes a word of ONLY uppercase OR ONLY lowercase &
    uses numeric_value_of(Letter) as a helper.
    Returns the value of the word as a sum of the individal character values'''
    alpha='abcdefghijklmnopqrstuvwxyz'
    wordValue = 0
    if (word.isupper()==True or word.islower()==True):
        for letter in Word:
            wordValue += numeric_value_ofL(letter)
        return wordValue
    else:
        return 'Word is not entirely UPPER/LOWER case'

words=['hellO','HO','OHAIYOU']
for word in words:
    print(numeric_value_ofW(word))
