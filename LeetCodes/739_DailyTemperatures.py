# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have 
# to wait after the ith day to get a warmer temperature. If there is no future 
# day for which this is possible, keep answer[i] == 0 instead.

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stx = []
    res = [0] * len(temperatures) #res arr with resp of 0

    for i in range(len(temperatures)):
        while stx and temperatures[i] > temperatures[stx[-1]]: #while act. temp bigger than temp in the top of stack
            prev = stx.pop()
            res[prev] = i - prev
        stx.append(i) #add the actual index to stack
    return res

temperatures = [73,74,75,71,69,72,76,73]
input()
print(dailyTemperatures(temperatures))