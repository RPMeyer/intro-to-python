#111111111111111111111111111111111111111
def cypher_C(Char):
    '''returns encyphered Char, as follows:
    if Char is not letter, it is not encyphered
    if Char is a lowercase OR uppercase letter, then it is encyphered'''

    alpha='abcdefghijklmnopqrstuvwxyz'
    cypher='mlkjihgfedcbazyxwvutsrqpon'
    if Char.isupper():
        Char=Char.lower()
        foundChar = alpha.find(Char)
        cypherChar = cypher[foundChar].capitalize()
    else:
        foundChar = alpha.find(Char)
        cypherChar = cypher[foundChar]
    if Char not in alpha:
        return Char
    return cypherChar

for Char in 'aBcD 1#&)':
    print('{} is encyphered to {}'.format(Char,cypher_C(Char)))

#----------------------------------------------------------------------
#22222222222222222222222222222222222222222222222222
def cypher_S(string):
    '''Uses character by character encyphering scheme from FUNCTION CYPHER_C(CHAR)
    to compute encyphered string and return string'''
    encypheredStringList=[]
    for i in string:
        encypheredStringList.append(cypher_C(i)) #HELPER FUNCTION
    return ''.join(encypheredStringList)

for String in ['Computer science is a must-take class!',"Uncled John's 5th?"]:
    print('plaintext string is: {0}'.format(String))
    print('and')
    print('cyphertext string is: {0}'.format(cypher_S(String)))
    print()
#----------------------------------------------------------------------
#33333333333333333333333333333333333333333333333333
def roll_right(String):
    '''Moves every character in string (String) to the right one place.
    RIGHTmost character becomes the LEFTmost. RETURNS resulting string'''
    dupeStringList=list(String)
    wordLength = len(dupeStringList)
    first = dupeStringList[(wordLength-1):]
    rest = dupeStringList[:(wordLength-1)]

    # print(first) #DEBUGGING
    # print(rest)

    return ''.join(first+rest)
for String in ['cat', 'tiger', 'parrot']:
    print('{} rolled right once is {}'.format(String,roll_right(String)))

#-----------------------------------------------------------------------
#444444444444444444444444444444444444444444444444444444

def roll_left(String):
    '''Moves every character in string (String) to the LEFT one place.
    LEFTmost character becomes the RIGHTmost. RETURNS resulting string'''
    dupeStringList=list(String)
    wordLength = len(dupeStringList)
    first = dupeStringList[:1]
    rest = dupeStringList[1:]

    # print(first) #DEBUGGING
    # print(rest)

    return ''.join(rest+first)
for String in ['cat', 'tiger', 'parrot']:
    print('{} rolled right once is {}'.format(String,roll_left(String)))

#-----------------------------------------------------------------------
#5555555555555555555555555555555555555555555555555555

def roll(String,n):
    '''RETURNS string (String) rolled (n) times.
    If (n)>0, String is rolled right (n) times.
    If (n)<0, String is rolled left (n) times.'''
    countN = n
    while countN>0:
        String = roll_right(String)
        countN-=1
    while countN<0:
        String = roll_left(String)
        countN+=1
    countN=n
    return String

for (String, n) in [('cat', 2),('tiger',-2),('parrot',3)]:
    print('{} rotated right {} times is {}'.format(String, n, roll(String,n)))

#-----------------------------------------------------------------------
#6666666666666666666666666666666666666666666666666 EXTRA CREDIT

def roll_then_encypher(String,n):
    '''rolls each word in string (String) (n) times, then encyphers the string.
    RETURNS the resulting string.'''
    newStringList=String.split()
    returnVal=[]

    for i in newStringList:
        returnVal.append(roll(i,n))

    returnVal = ' '.join(returnVal)

    newStringEncyphered=cypher_S(returnVal)

    return newStringEncyphered

String = 'a ab abc abcd abcde'
n=2
S=roll_then_encypher(String,n)
print('original string is {}'.format(String))
print('Rolled {} times, then encyphed, the sring is {}'.format(n, S))
