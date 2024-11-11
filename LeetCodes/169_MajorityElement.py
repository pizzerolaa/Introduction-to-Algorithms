# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

def majorityElement(nums: list[int]) -> int:
    #this is my solution
    aux = {}
    # res, val = 0, ''
    for num in nums:
        aux[num] = aux.get(num, 0) + 1 #here we save in aux all the repeated values of each num, ex: aux = {1: 3, 2: 4} where 1 is repeated 3 times

    # for i, j in aux.items(): #this works same that the max function below
    #     if res < j:
    #         res = j
    #         val = i
    #     return val

    return max(aux, key=aux.get) #here we can obtain the num with the max value 

nums = [3,2,3]
nums2 = [2,2,1,1,1,2,2]
print(majorityElement(nums2))