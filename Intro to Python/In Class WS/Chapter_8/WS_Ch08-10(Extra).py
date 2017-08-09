# ----------------------------------------
# Ws 8_10
#
# Write a function that returns a value of a word of lower case letters according to the following scheme
#value of word is the sum of each of its letters
#value is determined by position within alphabet squared


# ----------------------------------------
import re

def findAlpha(word):
    '''returns the position of letters in alphabet as a list'''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alphaValue=[]
    for i in word:
        foundLetter = alpha.find(i)
        alphaValue.append(foundLetter)
    return alphaValue

def valueOfWord(word):
    '''returns a value of a word (of lower case letters) according to the following scheme:
    Value of word is the sum of each of its letters. Value is determined by position within alphabet squared '''
    score=0
    valuesList = findAlpha(word)
    # print('valuesList consists of: {}'.format(valuesList))
    # print('length of word is {}'.format(len(valuesList)))
    for i in valuesList:
        print('value of i is {}'.format(i))
        score += i**2
        print('current score is: {}'.format(score))
    return score

#print(valueOfWord('hello'))


#cutting middle or a word out (if word is longer than 3) and reutnrs new words with missing middle
def stringWordChecker(sentence, length):
    '''returns the length of each word within sentence'''
    wordCount=len(sentence.split())
    listedSentence= re.split(pattern='\W+', string=sentence, maxsplit=wordCount)
    print(listedSentence)

stringWordChecker('hello, how are you today?', 2)
