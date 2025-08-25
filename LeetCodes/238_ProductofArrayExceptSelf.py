def productExceptSelf(nums: list[int]) -> list[int]:
    l = [] #create left var, here save a new list with a product of nums left to nums[i]
    r = [] #create right var, here save a new list with a product of nums right to nums[i]
    res = 1 # aux number to obtain products
    for num in nums:
        l.append(res)
        res *= num 
    # here l = [1, 1, 2, 6]
    
    res = 1
    for val in reversed(nums):
        r.append(res)
        res *= val
    r.reverse()
    #here r = [24, 12, 4, 1]

    return list(i * j for (i, j) in zip(l,r))
    #mult l and r to obtain [24, 12, 8, 6]
        

nums = [1,2,3,4]
input()
print(productExceptSelf(nums))