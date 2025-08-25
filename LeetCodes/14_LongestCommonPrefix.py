# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs: list[str]) -> str:
    #My solution, isn't good but isn't bad:
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    
    lcp = strs[0]

    for i in range(len(lcp)):
        for letter in strs[1:]:
            if i >= len(letter) or letter[i] != lcp[i]:
                return lcp[:i]
    return lcp

    #Solution that i want make, but idk about the existence of function startswith() lol:
    # Start by assuming the entire first string is the common prefix
    # commonStr = strs[0]
    # # Loop through all strings starting from the second one
    # for i in range(1, len(strs)):
    #     # While the current string does not start with the common prefix
    #     while not strs[i].startswith(commonStr):
    #         # Remove the last character from commonStr
    #         commonStr = commonStr[:-1]
    #         # If commonStr becomes empty, no common prefix exists
    #         if not commonStr:
    #             return ""
    # return commonStr

newStrs = ["flower","flow","flight"]
a = input()
print(longestCommonPrefix(newStrs))