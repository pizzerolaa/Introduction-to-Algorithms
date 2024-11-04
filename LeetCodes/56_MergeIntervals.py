"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""
def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0]) #we need sort the original matrix cuz in some cases we can have no sorting matrix
    res = [] #list to save the final result
    aux = intervals[0] #start in first interval like reference
    for i in range(1, len(intervals)): #if the actual interval overlapping with the next one, combine them
        if aux[1] >= intervals[i][0]:
            aux[1] = max(aux[1], intervals[i][1])
        else: #if non-overlapping, add the interval to res
            res.append(aux)
            aux = intervals[i]
    res.append(aux) #add the last processed interval
    return res
            

intervals = [[1,3],[0,6],[8,10],[11,15], [15, 19]]
input()

print(merge(intervals))