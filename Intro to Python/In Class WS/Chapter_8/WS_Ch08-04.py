# WS ch8_4
#
# Write a function updown(Word), which for any string does prints out what the
# example below shows if Word = ‘dog’:
# >>> updown(‘dog’)
# ‘d’
# ‘do’
# ‘dog’
# ‘do’
# ‘d’
#-------------------------------------

def updown(Word):
    '''for any string prints out the characters of string on new lines, starting from the first character
    incrementing until the string is printed entirely, then decreases on consecutive new lines again'''
    i=0
    switch=False
    while (i <= len(str(Word))):
        print(Word[:i])
        i+=1
        if(i==len(str(Word))):
            switch=True
            while switch==True:
                print(Word[:i])
                i-=1
                if i==0:
                    break
            break

updown('ohaiyou')
