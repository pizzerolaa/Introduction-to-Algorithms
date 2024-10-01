# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
from itertools import zip_longest

def mergeAlternately(word1: str, word2:str) -> str:
    nArr = []
    for i, j in zip_longest(word1, word2): #zip_longest works same that zip, but zip have limitations using the len of the most smallest str
        if i: #consider if i is not a empty str
            nArr.append(i)
        if j: #consider if j is not a empty str
            nArr.append(j)
    word = ''.join(nArr)
    return word

w1 = "ab"
w2 = "pqrs"
print(mergeAlternately(w1, w2))

word1 = "ab"
word2 = "pqrs"

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