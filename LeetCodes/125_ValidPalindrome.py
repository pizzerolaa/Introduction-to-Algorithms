# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
import re, string

def isPalindrome(s: str) -> bool:
    s = re.sub('[%s]' % re.escape(string.punctuation), '', s).lower()
    s = "".join(s.split())
    
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1 
    return True

s = "A man, a plan, a canal: Panama"
input()
print(isPalindrome(s))