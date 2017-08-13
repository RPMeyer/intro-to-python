# Ws ch8_7
#
# Write a function, num_words_in(Sentence), which returns the number of words
# in Sentence.
#-------------------------------------
def num_words_in(Sentence):
    '''returns the number of words in a sentence (Sentence).'''
    return len(Sentence.split())

print(num_words_in(Sentence='Oh hello there.'))
