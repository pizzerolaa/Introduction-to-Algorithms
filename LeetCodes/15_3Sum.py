# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort() #we sort to facilate the search
    aux = []
    
    for x in range(len(nums) - 2): #first index
        if x > 0 and nums[x] == nums[x - 1]:
            continue #skip duplicates for first num
        y, z = x + 1, len(nums) - 1
        while y < z: # we use Two Pointers technique
            current_sum = nums[x] + nums[y] + nums[z]

            if current_sum == 0:
                aux.append([nums[x], nums[y], nums[z]])
                y += 1
                z -= 1
                while y < z and nums[y] == nums[y - 1]: #skip duplicates for y and z (second and third nums)
                    y += 1
                while y < z and nums[z] == nums[z + 1]:
                    z -= 1
            elif current_sum < 0:
                y += 1
            else:
                z -= 1
    return aux

nums = [-1,0,1,2,-1,-4]
input()
print(threeSum(nums))
