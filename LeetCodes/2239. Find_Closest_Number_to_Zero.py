# Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
# If there are multiple answers, return the number with the largest value.

# Example 1:

# Input: nums = [-4,-2,1,4,8]
# Output: 1
# Explanation:
# The distance from -4 to 0 is |-4| = 4.
# The distance from -2 to 0 is |-2| = 2.
# The distance from 1 to 0 is |1| = 1.
# The distance from 4 to 0 is |4| = 4.
# The distance from 8 to 0 is |8| = 8.
# Thus, the closest number to 0 in the array is 1.

def find_closes_number(nums: list[int]) -> int:
    #this code has a O(n) time complexity
    res = nums[0]
    for num in nums:
        if abs(num) < abs(res):
            res = num
    if abs(res) in nums:
        return abs(res)
    return res

nums = [-4, -2, 1, 4, 8]
input()
print(find_closes_number(nums=nums))

#this code nahhh
# def find_closes_number2(nums: list[int]) -> int:
#     #this code has a O(n log n) time complexity
#     nums.sort()
#     res = nums[0]
#     for num in nums:
#         if abs(num) < abs(res) or (abs(num) == abs(res) and num > res):
#             res = num
#     return res