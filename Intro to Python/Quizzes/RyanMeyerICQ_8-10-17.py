#Write a function repeat_L(Letter,n), which returns Letter (n) times.
import re
def repeat_L(Letter,n):
    '''returns Letter (n) times'''
    print(type(Letter))
    print(type(n))
    return Letter*n

for (Letter,n) in [('r',3),('V',5),('w',2)]:
    print(repeat_L(Letter,n))

#-----------------------------------
def repeat_letters_in(Word):
    '''passes word (Word) composed entirely of letters and RETURNS
    a word with the first letter of Word repeated once, second letter repeated twice,
    third letter repeated thrice, ... , (n)th repeated (n) times.
    USES repeat_L(Letter,n) AS HELPER'''
    counter=1
    newWord=''
    for i in Word:
        test=i*counter
        newWord+=test
        counter+=1
    return newWord

Words=['a','at','aim','back']
for Word in Words:
    print(Word, repeat_letters_in(Word))

#-----------------------------------
def repeat_letters_in_each_word_in(Sentence):
    '''takes sentence of only letters seperated by a single space and ending with a period...
    and RETURNS a sentence of words seperated by a single space and ending with a period, where each
    word has its letters repeated.
    USES repeat_letters_in(Word) AS HELPER FUNCTION'''
    newSent = []
    if Sentence.find('.')==len(Sentence)-1:
        holder=Sentence[len(Sentence)-1:]
        noPeriod=Sentence[:len(Sentence)-1]
        for i in noPeriod.split():
            newSent.append(repeat_letters_in(i))
        newSent.append(holder)
    return ' '.join(newSent)


Sentence = 'Brevity is the soul of wit.'
print('Original sentence: {}'.format(Sentence))
print('Sentence with repeat letters in each word: {}'.format(repeat_letters_in_each_word_in(Sentence)))
