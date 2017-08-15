def B_sequence(n,m):
    '''returns the first (m) terms of a sequence that starts with int (n).
    Sequence is (2*abs(previous_term - 2))'''
    previous_term=0
    sequenceList=[n]
    previous=n
    for i in range (n,n+m-1,1):
        previous=(2*abs(previous-2))
        sequenceList.append(previous)
    return sequenceList
print(B_sequence(5,7))

n=1
while (sum(B_sequence(5,n)))<=1000:
    n+=1
print(n)
print(sum(B_sequence(5,n)))

def frontToBack(Word,n):
    '''returns the first (n) letters of (Word) word appended to the beginning of Word'''
    return Word[n:]+Word[:n]
print(frontToBack('aloha',3))

Word='tiberius'
for n in range(len(Word)):
    print(n, frontToBack(Word,n))

def frontToBack_repeated(Word, n, repeat):
    newWord=Word
    for i in range(repeat):
        newWord=frontToBack(newWord,n)
    return newWord

print(frontToBack_repeated(Word='tiberius', n=3, repeat=2))

repeat=1
while not (frontToBack_repeated(Word='tiberius', n=3, repeat=repeat)==Word):
    print(frontToBack_repeated(Word='tiberius', n=3, repeat=repeat))
    repeat+=1
print(frontToBack_repeated(Word='tiberius', n=3, repeat=repeat))

print(repeat)
