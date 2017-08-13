# HW:2,3,6, 7,8,10
#
#
# Youtube: Write a function rev_each_word_in(Sentence), that takes a
# sentence of words that may or may not have a final period & which
# returns a sentence, each of word of which is reversed. You can
# assume that all letters are lowercase with no punctuation except the
# final period. For example
#
#
# If Sentence = 'to be or not to be that is the question.'
# Modify so that Ouack and Quack are spelled correctly.
prefixes = "JKLMNOPQ"
suffix = "ack"
prefixList = list(prefixes)

for letter in prefixList:
    if((letter == 'O') or (letter =='Q')):
        prefixList[prefixList.index(letter)]=letter+'u'
    print(prefixList[prefixes.find(letter)]+suffix)
