# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
    # Input: strs = ["eat","tea","tan","ate","nat","bat"]
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    # Explanation:
        # There is no string in strs that can be rearranged to form "bat".
        # The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
        # The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
    # Input: strs = [""]
    # Output: [[""]]

# Example 3:
    # Input: strs = ["a"]
    # Output: [["a"]]

from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    aux = defaultdict(list)

    for str in strs:
        sort_str = tuple(sorted(str))  # O(m * log(m))
        aux[sort_str].append(str)
    
    return list(aux.values())

strs = ["eat","tea","tan","ate","nat","bat"]
input()
print(group_anagrams(strs=strs))

# #bro this is my first solution and i have time limit exceed lol :((
    # res = []
    # unique = set() #save each sort tuple only one time, prevent duplicates

    # for i in range(len(strs)):
    #     #store the sorted version of each string, so that two anagrams have the same sorted tuple
    #     sort_str = tuple(sorted(strs[i]))

    #     if sort_str not in unique: #prevent duplicates
    #         helper = []
    #         for j in range(i, len(strs)):
    #             if sort_str == tuple(sorted(strs[j])):
    #                 helper.append(strs[j])
    #         unique.add(sort_str)
    #         res.append(helper)

    # return res