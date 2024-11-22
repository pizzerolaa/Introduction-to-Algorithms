# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s: str) -> bool:
    #for this case, we've a time complexity: O(n) 
    stx = []
    for char in s:
        if char in "({[":
            stx.append(char)
        else:
            if not stx:
                return False
            if (char == ")" and stx[-1] == "(") or \
                (char == "}" and stx[-1] == "{") or \
                (char == "]" and stx[-1] == "["):
                stx.pop()
            else:
                return False
    return len(stx) == 0
        
s = "]"
input()
print(isValid(s))