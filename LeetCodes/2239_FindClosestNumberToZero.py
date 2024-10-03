# Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
# If there are multiple answers, return the number with the largest value.

def findClosestNumber(nums: list[int]) -> int:
    min = nums[0]
    for i in range(len(nums)):
        if abs(nums[i]) < abs(min):
            min = nums[i]
    if abs(min) in range(len(nums)): #compare if min positive is in the list
        return abs(min)
    return min


ex = [-4,-2,1,4,8]
#ex2 = [2, -1, 1]
ex3 = [-10000, -10000]
ex2 = [int(x) for x in input().split()]
print(findClosestNumber(ex2))