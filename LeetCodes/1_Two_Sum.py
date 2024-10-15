# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums: list[int], target: int) -> list[int]:
    #this solution have a complex O(n) more efficiently, here we use a dict for save the nums and their index
    aux = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in aux:
            return [aux[comp], i]
        aux[num] = i
    return [] #if we don't found a couple 
    
    # This solution have a complex O(n²) in the worst case, but obviusly is more faster that others solutions
    # aux = set(nums)
    # for i in range(len(nums)):
    #     comp = target - nums[i]
    #     if comp in aux:
    #         for j in range(i + 1, len(nums)):
    #             if nums[j] == comp:
    #                 return [i, j]
    # return []

newNums = [2,7,11,15]
newTarget = 9
input()
print(twoSum(newNums, newTarget))