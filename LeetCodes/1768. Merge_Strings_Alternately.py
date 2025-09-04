# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

def merge_alternately(word1: str, word2: str) -> str:
    #Time: O(N1 + N2)
    n1, n2 = len(word1), len(word2)
    p1, p2 = 0, 0
    merge = []

    word = 1
    while p1 < n1 and p2 < n2:
        if word == 1:
            merge.append(word1[p1])
            p1 += 1
            word = 2
        else:
            merge.append(word2[p2])
            p2 += 1
            word = 1
    
    while p1 < n1:
        merge.append(word1[p1])
        p1 += 1
    
    while p2 < n2:
        merge.append(word2[p2])
        p2 += 1

    return "".join(merge)
        

w1 = "ab"
w2 = "pqrs"
input()
print(merge_alternately(word1=w1, word2=w2))

#My last code
# def mergeAlternately(word1: str, word2:str) -> str:
#     nArr = []
#     for i, j in zip_longest(word1, word2): #zip_longest works same that zip, but zip have limitations using the len of the most smallest str
#         if i: #consider if i is not a empty str
#             nArr.append(i)
#         if j: #consider if j is not a empty str
#             nArr.append(j)
#     word = ''.join(nArr)
#     return word

# # First iteration: i = 'a', j = 'p'
# if 'a':  # True, adds 'a'
# if 'p':  # True, adds 'p'

# # Second iteration: i = 'b', j = 'q'
# if 'b':  # True, adds 'b'
# if 'q':  # TRue, adds 'q'

# # Third iteration: i = '', j = 'r'
# if '':   # False, adds nothing
# if 'r':  # True, add 'r'

# # Fourth iteration: i = '', j = 's'
# if '':   # False, adds nothing
# if 's':  # True, add 's'