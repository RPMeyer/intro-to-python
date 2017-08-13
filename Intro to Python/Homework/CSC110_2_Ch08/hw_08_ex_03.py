# HW:3,6, 7,8,10
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

# Encapsulate in a function named count_letters, and generalize it so that it accepts the string and the letter as arguments.
# Make the function return the number of characters, rather than print the answer. The caller should do the printing:
# fruit = "banana"
# count = 0
# for char in fruit:
#     if char == "a":
#         count += 1
# print(count)

def count_Letters(string, letter):
    '''returns number of characters defined as (Letter) in a string (string)'''
    fruit = str(string)
    count = 0
    for char in fruit:
        if char == letter:
            count += 1
    return count

print(count_Letters(string='bananaaaaaaaaa', letter='a'))
