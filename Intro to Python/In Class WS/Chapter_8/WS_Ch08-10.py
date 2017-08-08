# ----------------------------------------
# Ws 8_10
#
# Write a function that takes word of lowercase letters (plaintext) and which
# returns an enciphered word (cypher text) using a circular Caesar cypher for
# each letter.
# ----------------------------------------

def ceasarCypher(word, shift):
    '''takes word of lowercase letters (plaintext) and returns an enciphered word (cypher text)
    using a circular Caesar cypher for each letter.'''

    alphaList=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha='abcdefghijklmnopqrstuvwxyz'
    nuericList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    zippedList= list(zip(alphaList,nuericList))
    cypher=[]
    for i in word:
        foundLetter = alpha.find(i)
        if (foundLetter+shift >=26):
            x=(foundLetter+shift)%26
            cypher.append(zippedList[x][0])
        else:
            cypher.append(zippedList[foundLetter+shift][0])
    return ''.join(cypher)

words=['hello', 'goodbye', 'maybe','find','a','way','to','not','use a for loop']
sentence="this is a sentence to test this cypher"
for word in words:
    print(ceasarCypher(word, 24))
