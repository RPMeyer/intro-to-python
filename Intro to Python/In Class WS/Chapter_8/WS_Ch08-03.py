# WS 8_3
#
# Write a function numeric_value_ofS(Sentence), which takes a Sentence,
# which is a string consisting of words separated by spaces and where each
# word consists only of lowercase and uppercase letters, and which returns the
# sum of the numeric value of Sentence. Uses numeric_value_of(Word).
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
    if (Word.isupper()==True or Word.islower()==True):
        for letter in Word:
            wordValue += numeric_value_ofL(letter)
        return wordValue
    else:
        return 'Word is not entirely UPPER/LOWER case'

def numeric_value_ofS(Sentence):
    '''takes a Sentence which is a string consisting of words separated by spaces and where each
    word consists only of lowercase and uppercase letters, and which returns the
    sum of the numeric value of Sentence.
    Uses numeric_value_of(Word).'''
    alpha='abcdefghijklmnopqrstuvwxyz'
    sentenceValue = 0

    for word in Sentence.split():
        if (word.isupper()==True or word.islower()==True):
            sentenceValue+= numeric_value_ofW(word)
        else:
            return 'That sentence is not ONLY UPPER/LOWER case'
    return sentenceValue

print(numeric_value_ofS('this IS A TesT OF THE SENTENCE'))
print(numeric_value_ofS('this IS A TEST OF THE SENTENCE'))
