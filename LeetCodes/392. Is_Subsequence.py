# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by d
# eleting some (can be none) of the characters without disturbing the relative positions 
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def is_subsequence(s: str, t: str) -> bool:
    #Time: O(N) Memory O(1)
    i = 0
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    
    return i == len(s)

s = "aec"
t = "abcde"
input()
print(is_subsequence(s=s, t=t))

#another solution (tbh it's my first lol)
# def isSubsequence(s: str, t: str) -> bool:
#     l_find = -1
    
#     for char in s:
#         find = False
        
#         for i in range(l_find + 1, len(t)):
#             if t[i] == char:
#                 l_find = i
#                 find = True
#                 break

#         if not find:
#             return False
#     return True