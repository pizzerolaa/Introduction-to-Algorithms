# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums: list[int], target: int) -> list[int]:
    new_nums = [(nums[i], i) for i in range(len(nums))]
    new_nums.sort()
    
    l, r = 0, len(new_nums) - 1
    
    while l < r:
        suma = new_nums[l][0] + new_nums[r][0]
        if suma == target:
            return sorted([new_nums[l][1], new_nums[r][1]])
        elif suma < target:
            l += 1
        else:
            r -= 1
    
    return []

nums = [3,2,4]
target = 6
input()
print(two_sum(nums=nums, target=target))

#this solution have a complex O(n) more efficiently, here we use a dict for save the nums and their index
# def twoSum(nums: list[int], target: int) -> list[int]:
#     aux = {}
#     for i, num in enumerate(nums):
#         comp = target - num
#         if comp in aux:
#             return [aux[comp], i]
#         aux[num] = i
#     return [] #if we don't found a couple 
    
# This solution have a complex O(n²) in the worst case, but obviusly is more faster that others solutions
#def twoSum(nums: list[int], target: int) -> list[int]:
# aux = set(nums)
# for i in range(len(nums)):
#     comp = target - nums[i]
#     if comp in aux:
#         for j in range(i + 1, len(nums)):
#             if nums[j] == comp:
#                 return [i, j]
# return []