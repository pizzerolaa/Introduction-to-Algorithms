# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def containsDuplicate(nums: list[int]) -> bool:
    aux = set(nums) #set delete the repeated data (nums)
    if len(aux) == len(nums): #compare the lenght of set (aux) and array (nums)
        return False #False if both have the same len
    else:
        return True # True both don't have the same len (reapeated number)

newNums = [1,2,3,4]
print(containsDuplicate(newNums))