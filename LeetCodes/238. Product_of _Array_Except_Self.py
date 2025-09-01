# Given an integer array nums, return an array answer such that answer[i] is equal to the 
# product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
    # Input: nums = [1,2,3,4]
    # Output: [24,12,8,6]

# Example 2:
    # Input: nums = [-1,1,0,-3,3]
    # Output: [0,0,9,0,0]
import math

def product_except_self(nums:list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n -1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res

nums = [1, 2, 3, 4]
input()
print(product_except_self(nums=nums))

#this my first code, it works but has a O(n^2) complexity
# def product_except_self(nums:list[int]) -> list[int]:
#     res = []
#     for i in range(len(nums)):
#         aux = nums[:i] + nums[i+1:]
#         res.append(math.prod(aux))
#     return res

#this code has O(n) complexity but is more confused
# def productExceptSelf(nums: list[int]) -> list[int]:
#     l = [] #create left var, here save a new list with a product of nums left to nums[i]
#     r = [] #create right var, here save a new list with a product of nums right to nums[i]
#     res = 1 # aux number to obtain products
#     for num in nums:
#         l.append(res)
#         res *= num 
#     # here l = [1, 1, 2, 6]
    
#     res = 1
#     for val in reversed(nums):
#         r.append(res)
#         res *= val
#     r.reverse()
#     #here r = [24, 12, 4, 1]

#     return list(i * j for (i, j) in zip(l,r))
#     #mult l and r to obtain [24, 12, 8, 6]

