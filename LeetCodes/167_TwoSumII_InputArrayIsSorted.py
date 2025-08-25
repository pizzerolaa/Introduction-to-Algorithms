# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. Let these two numbers be 
# numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

def twoSum(numbers: list[int], target: int) -> list[int]:
    #in this case we have the sum, but using the Two Pointers technique.
    l, r = 0, len(numbers) - 1
    res = []
    while l < r:
        aux = numbers[l] + numbers[r]
        if aux == target:
            res = [l + 1, r + 1]
            break
        elif aux < target:
            l += 1
        else:
            r -= 1
    
    return res

nums = [2, 7, 11, 15] 
target = 9
input()
print(twoSum(nums, target))