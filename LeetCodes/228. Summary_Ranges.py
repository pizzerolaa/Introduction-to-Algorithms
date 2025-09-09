# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
# That is, each element of nums is covered by exactly one of the ranges, and there is no integer x 
# such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:
    # "a->b" if a != b
    # "a" if a == b

def summary_ranges(nums: list[int]) -> list[str]:
    aux = []
    res = []

    for num in nums:
        aux.append(num)
        if num + 1 not in nums:
            if len(aux) == 1:
                res.append(f"{aux[0]}")
            else:
                res.append(f"{aux[0]}->{aux[-1]}")
            aux.clear()

    return res

nums = [-1, 2, 3, 4, 5, 8]
input()
print(summary_ranges(nums))

#my last code
# res = []
# aux = []
# for i in range(len(nums)):
#     #check if is the first num or if the actual num is consecutive to the prev num
#     if i == 0 or nums[i] == nums[i-1] +1:
#         aux.append(nums[i])
#     else:
#         #if secuense broke, add the finded range
#         if len(aux) > 0:
#             if len(aux) == 1:
#                 res.append(str(aux[0])) #in case that have one num, add only one num ["7"] and not ["7->7"] 
#             else:
#                 res.append(f"{aux[0]}->{aux[-1]}") #add range
#             aux = [nums[i]] #reset aux with new num

# #add last group if this exist
# if len(aux) > 0:
#     if len(aux) == 1:
#         res.append(str(aux[0]))
#     else:
#         res.append(f"{aux[0]}->{aux[-1]}")
# return res