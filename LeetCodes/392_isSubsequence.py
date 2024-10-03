# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
# of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
from itertools import zip_longest

def isSubsequence(s: str, t: str) -> bool:
    l_find = -1
    
    for char in s:
        find = False
        
        for i in range(l_find + 1, len(t)):
            if t[i] == char:
                l_find = i
                find = True
                break

        if not find:
            return False
    return True

s1 = input()
t1 = 'acb'
print(isSubsequence(s1, t1))