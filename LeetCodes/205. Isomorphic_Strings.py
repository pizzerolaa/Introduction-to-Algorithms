# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving 
# the order of characters. No two characters may map to the same character, but a character may map to itself.


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
            return False
        
    aux_t = {}
    aux_s = {}
    
    for index, char_s in enumerate(s):
        char_t = t[index]
        if char_s in aux_t and aux_t[char_s] != char_t:
            return False
        if char_t in aux_s and aux_s[char_t] != char_s:
            return False
        aux_t[char_s] = char_t
        aux_s[char_t] = char_s

    return True

s = "egg"
t = "add"
input()
print(is_isomorphic(s, t))