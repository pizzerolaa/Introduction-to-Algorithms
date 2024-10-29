def summaryRanges(nums: list[int]) -> list[str]:
    res = []
    aux = []

    for i in range(len(nums)):
        #check if is the first num or if the actual num is consecutive to the prev num
        if i == 0 or nums[i] == nums[i-1] +1:
            aux.append(nums[i])
        else:
            #if secuense broke, add the finded range
            if len(aux) > 0:
                if len(aux) == 1:
                    res.append(str(aux[0])) #in case that have one num, add only one num ["7"] and not ["7->7"] 
                else:
                    res.append(f"{aux[0]}->{aux[-1]}") #add range
                aux = [nums[i]] #reset aux with new num
    
    #add last group if this exist
    if len(aux) > 0:
        if len(aux) == 1:
            res.append(str(aux[0]))
        else:
            res.append(f"{aux[0]}->{aux[-1]}")

    return res

nums = [0,1,2,4,5,7]
input()
print(summaryRanges(nums))