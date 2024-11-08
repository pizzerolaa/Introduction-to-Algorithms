# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from collections import defaultdict # this reduce the need for nested loops

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)

    for string in strs:
        sort_str = tuple(sorted(string)) #sort the string and use it as key
        res[sort_str].append(string) #append the original str to the list to the sorted tuple
    
    return list(res.values()) #convert the defaultdict values to a matrix or list[list[str]]


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

strs = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
input()
print(groupAnagrams(strs))
