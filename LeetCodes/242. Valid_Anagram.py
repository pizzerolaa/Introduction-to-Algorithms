from collections import Counter
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
    # Input: s = "anagram", t = "nagaram"
    # # Output: true

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    aux = Counter(s)
    for letter in t:
        if aux[letter] <= 0:
            return False
        aux[letter] -= 1
    
    return True

s = "a"
t = "ab"
input()
print(is_anagram(s, t))

#Simple solution and most efficent:
# def is_anagram(s: str, t: str) -> bool:
#     return Counter(s) == Counter(t) 