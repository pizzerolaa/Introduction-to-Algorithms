# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Example 1:
    # Input: nums = [1,2,3,1]
    # Output: true
# Explanation:
    # The element 1 occurs at the indices 0 and 3.

def contains_duplicate(nums: list[int]) -> bool:
    hashm = set()
    for i in range(len(nums)):
        if nums[i] in hashm:
            return True
        else:
            hashm.add(nums[i])
    return False
    
nums = [1, 2, 3, 1]
print(contains_duplicate(nums))

# Most efficent:
## def contains_duplicate(nums: list[int]) -> bool:
    # nums_new = set(nums)
    # if len(nums_new) == len(nums):
    #     return False
    # else:
    #     return True