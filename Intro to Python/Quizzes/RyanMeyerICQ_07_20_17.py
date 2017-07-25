import math
vowelsList = ['a', 'e', 'i', 'o', 'u']
Words =['hawaii', 'aloha', 'pineapple', 'tops']

#make FUNCTIONS!!@$#$^YHW
def is_vowel(word):
    ''' determine if letter in string is a vowel'''
    vowelsList = ['a', 'e', 'i', 'o', 'u']
    for i in word:
        if i in vowelsList:
            return True

def is_consonant(word):
    ''' determine if letter in string is a consonant'''
    vowelsList = ['a', 'e', 'i', 'o', 'u']
    for i in word:
        if i not in vowelsList:
            return True

def ratio_of_vwls2cons(word):
    vowelCount=0
    consCount =0

    for letter in word:
        if is_vowel(letter):
            vowelCount += 1
        else:
            consCount += 1
    return (vowelCount/consCount)

for Letter in 'aloha':
    if is_vowel(Letter):
        print(Letter, end = ' ')

print('\n')

for Letter in 'aloha':
    if is_consonant(Letter):
        print(Letter, end = ' ')

print('\n')

for Word in Words:
    R = ratio_of_vwls2cons(Word)
    print(Word, round(R,2))
