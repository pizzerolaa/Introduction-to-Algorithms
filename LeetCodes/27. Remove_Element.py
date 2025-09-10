# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, 
# you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not 
# equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

def remove_element(nums: list[int], val:int) -> int:
    k, r= 0, len(nums) - 1

    while k <= r:
        if nums[k] == val and nums[r] != val:
            nums[k], nums[r] = nums[r], nums[k]
            r -= 1
            k += 1
        elif nums[r] == val:
            r -= 1
        else:
            k += 1
    
    return k

nums = [3,2,2,3]
val = 3
input()
print(remove_element(nums, val))


#another solution, but this doesnt make the swap correctly
# k = 0
#     for i in range(len(nums)):
#         if nums[i] != val:
#             nums[k] = nums[i]
#             k += 1   
#     return k

#my first solution:
# def removeElement(nums: list[int], val: int) -> int:
#     count = 0
#     while count < len(nums):
#         if nums[count] == val:
#             nums.pop(count)
#         else:
#             count+=1
#     return count
