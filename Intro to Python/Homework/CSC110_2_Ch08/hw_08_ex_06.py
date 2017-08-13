# HW:6,7,8,10
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

#Print out a neatly formatted multiplication table, up to 12 x 12.

def multiTable(base1=12, base2=12):
    '''Prints out a neatly formatted multiplication table, up to (base1)x(base2)'''
    row = 0
    column = 0
    while (row <= base1):
        for i in range(0,base1+1,1):
            print ('{0:{width}}'.format(i*column,width=5),end='')
            if(i==base1):
                column+=1
        print()
        row+=1

multiTable()
