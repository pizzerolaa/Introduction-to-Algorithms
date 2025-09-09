# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

def longest_consecutive(nums: list[int]) -> int:
    aux = set(nums)
    count = 0
    for num in aux:
        if num - 1 not in aux:
            next_v = num + 1
            lengt = 1
            while next_v in aux:
                lengt += 1
                next_v += 1
            count = max(count, lengt)
    return count
        
nums = [5,6,3,7,2,1,8,9,0]
input()
print(longest_consecutive(nums))

