vowelsList = ['a', 'e', 'i', 'o', 'u']

#make FUNCTIONS!!@$#$^YHW
def is_vowel(word):
    ''' determine if letter in string is a vowel'''
    vowelsList = ['a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter in vowelsList:
            print(letter)

def is_consonant(word):
    ''' determine if letter in string is a consonant'''
    vowelsList = ['a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter not in vowelsList:
            print(letter)

is_vowel('aloha')
is_consonant('aloha')
