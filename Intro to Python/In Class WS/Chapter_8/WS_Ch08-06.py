# Ws ch8_6
#
# Write a function, count_words_in_1(Sentence), that does the same thing as the
# previous function except that y is also a vowel, but only if it is at the end of the
# word.
#-------------------------------------
def sometimesY(Word):
    '''returns True is the vowel (y) is at the end of a word (Word)'''
    if (Word[(len(Word))-1:])=='y':
        return True
    else:
        return False

def vowelCounter(Word, limit=2):
    '''counts vowels in a word, returns word if number of vowels surpasses limit'''
    vowelList = ['a','e','i','o','u']
    vowelCount=0
    for i in Word:
        if i in vowelList:
            vowelCount+=1
            if vowelCount >=limit:
                return True

def count_words_in(Sentence, lowerBound=3,upperBound=7, vowelCount=2):
    '''returns the number of words in Sentence that have between
    3 and 7 letters and which contain at least 2 vowels,
    where vowels are taken to be the letters {‘a’,’e’,’I’,’o’,’u’}'''
    wordCount=0
    sentenceList = Sentence.split()
    for word in sentenceList:
        if (word[lowerBound:upperBound]) and vowelCounter(word)==True:
            wordCount+=1
    return wordCount

def count_words_in_1(Sentence, lowerBound=3,upperBound=7, vowelCount=2):
    '''same as count_words_in(Sentence), except y is also a vowel, but only if it is at the end of word (Word).'''
    wordCount=0
    sentenceList = Sentence.split()
    for word in sentenceList:
        if (word[lowerBound:upperBound]) and vowelCounter(word)==True and sometimesY(word)==True:
            wordCount+=1
    return wordCount

sometimesY('hello')
print(count_words_in('this is a hhhhhhoohhhhhhh test sssssssss sentence'))
print(count_words_in_1('this is a hhhhhhoohhhhhhhhy test sssssssss sentence'))
