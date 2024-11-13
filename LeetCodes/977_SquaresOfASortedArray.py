# Given an integer array nums sorted in non-decreasing order, return an 
# array of the squares of each number sorted in non-decreasing order.

def sortedSquares(nums: list[int]) -> list[int]:
    #in this case we use the 2 pointers technique, it's most easy and faster do this if we don't use this technique
    l, r = 0, len(nums) - 1
    aux = []
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            aux.append(nums[l]**2)
            l += 1
        else:
            aux.append(nums[r]**2)
            r -= 1
    
    aux.sort()
    return aux

    #ex. without use the two pointers technique
    nums = [i**2 for i in nums]
    return sorted(nums)

nums = [-4,-1,0,3,10]
input()
print(sortedSquares(nums))