def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    col_seq =[]
    while n != 1:
        col_seq.append(n)
        #print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    #print(n, end=".\n")
    col_seq.append(n)
    return col_seq

print(seq3np1(100))
print(seq3np1(1000))

# def findMaxLengthList(n):
#     '''sort for highest length list'''
#     listLength = []
#     lenMax = []
#     x= n
#     while i<=x:
#         lenMAx = seq3np1(n)
#         if listLength < len(listMax):
#             listLength = seq3np1(n-(n-1))
#             print(listLength)
#         n=n-1
#     return listMax
#
# print(findMaxLengthList(100))
