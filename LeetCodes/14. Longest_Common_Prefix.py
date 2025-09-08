# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

strs = ["flower","flow","flight"]
input()
print(longest_common_prefix(strs))


#hahaha nahh i make this shi using the Trie Data Structure
# def longest_common_prefix(strs: list[str]) -> str:
#     if not strs or len(strs) == 0:
#         return ""
    
#     if len(strs) == 1:
#         return strs[0]
    
#     trie = {}

#     for s in strs:
#         current = trie
#         for char in s:
#             index = ord(char) - ord('a')
#             if index not in current:
#                 current[index] = {'count': 0}
#             current[index]['count'] = current[index].get('count', 0) + 1
#             current = current[index]
#         current['is_end'] = True
    
#     prefix = ""
#     current = trie
#     total_words = len(strs)

#     while True:
#         children = [k for k in current.keys() if isinstance(k, int)]
#         if len(children) != 1 or current.get('is_end'):
#             break
#         child_idx = children[0]
#         if current[child_idx]['count'] != total_words:
#             break
#         prefix += chr(child_idx + ord('a'))
#         current = current[child_idx]
#     return prefix

#My first solution, isn't good but isn't bad:
    # if len(strs) == 0:
    #     return ""
    # if len(strs) == 1:
    #     return strs[0]
    
    # lcp = strs[0]

    # for i in range(len(lcp)):
    #     for letter in strs[1:]:
    #         if i >= len(letter) or letter[i] != lcp[i]:
    #             return lcp[:i]
    # return lcp