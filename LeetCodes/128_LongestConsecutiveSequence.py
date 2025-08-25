# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
def longestConsecutive(nums: list[int]) -> int:
    #joder tío que la hemos liado despues de 2 horas, i don't need explain this code, is very simple
    aux = set(nums)
    count = 0
    for i in range(len(nums)):
        if nums[i] - 1 not in aux: #if the actual num - 1 not in the hash continue
            next = nums[i] + 1
            lenght = 1 
            while next in aux:
                lenght += 1
                next += 1
            count = max(count, lenght)
    return count

nums = [9,1,4,7,3,-1,0,5,8,-1,6]
input()
print(longestConsecutive(nums))