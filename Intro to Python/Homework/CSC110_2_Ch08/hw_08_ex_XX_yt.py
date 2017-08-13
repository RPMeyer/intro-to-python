# Youtube: Write a function rev_each_word_in(Sentence), that takes a
# sentence of words that may or may not have a final period & which
# returns a sentence, each of word of which is reversed. You can
# assume that all letters are lowercase with no punctuation except the
# final period. For example
#
# If Sentence = 'to be or not to be that is the question.'
# Then the output should be:
# ot eb ro ton ot eb taht si eht noitseuq.
#
# If Sentence = 'to be or not to be that is the question'
# Then the output should be:
# ot eb ro ton ot eb taht si eht noitseuq

def rev_each_word_in(Sentence):
    '''takes a sentence of words that may/not have a final period & which returns
    a sentence, each of word of which is reversed. You can assume
    that all letters are lowercase with no punctuation EXCEPT the final period'''
    if Sentence.find('.')==len(Sentence)-1: #checks for period at the end of Sentence
        holder=Sentence[len(Sentence)-1:] #stores '.' to be appended after misc
        noPeriod=(Sentence[:len(Sentence)-1]) #assigns noPeriod the contents of Sentence to the last place, thusly removing '.'
        test= noPeriod.split() #stores as a list
        for word in test:
            test[test.index(word)]=word[::-1] #reverses each word individually found within test[]
        test.append(holder) #replaces the '.' at the end of test[]
    else:
        test=Sentence.split()
        for word in test:
            test[test.index(word)]=word[::-1]

    return ' '.join(test)

print(rev_each_word_in(Sentence='to be or not to be that is the question.'))
print(rev_each_word_in(Sentence='to be or not to be that is the question'))
