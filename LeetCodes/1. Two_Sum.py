# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
# auxlanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums: list[int], target: int) -> list[int]:
    #this solution have a complex O(n) more efficiently, here we use a dict for save the nums and their index
    aux = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in aux:
            return [aux[diff], index]
        aux[num] = index
    return []

nums = [3,2,4]
target = 6
input()
print(two_sum(nums=nums, target=target))

#my other solution bro, using two pointers lol:
# def twoSum(nums: list[int], target: int) -> list[int]:
#   new_nums = [(nums[i], i) for i in range(len(nums))]
#   new_nums.sort()

#   l, r = 0, len(new_nums) - 1

#   while l < r:
#       suma = new_nums[l][0] + new_nums[r][0]
#       if suma == target:
#           return ([new_nums[l][1], new_nums[r][1]])
#       elif suma < target:
#           l += 1
#       else:
#           r -= 1

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