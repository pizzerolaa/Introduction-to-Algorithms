# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
def isAnagram(s: str, t: str) -> bool:
    if len(s) < len(t): # if s is smallest than t, return False
        return False
    #re-use code of leetcode 383 lol
    aux = {}

    for char in t:
        aux[char] = aux.get(char, 0) + 1

    for char in s:
        if char not in aux or aux[char] == 0:
            return False
        aux[char] -= 1
    return True

newS = "rat"
newT = "car"
input()
print(isAnagram(newS, newT))