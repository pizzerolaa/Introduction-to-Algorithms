# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

def trap(height: list[int]) -> int:
    #in this case we use the Two Pointers technique, we have the same time complexity O(n) but in space we have O(1)
    l, r = 0, len(height) - 1
    heightL, heightR = height[l], height[r]
    res = 0

    while l < r:
        if heightL <= heightR:
            l += 1
            h = height[l]
            if h > heightL:
                heightL = h
            else:
                res += heightL - h
        else:
            r -= 1
            if (h:= height[r]) > heightR: # h := height[r] is the same that h = height[r], this operator assing and compare this value in only one line
                heightR = h
            else:
                res += heightR - h
    
    return res

    # #this solution have O(n) time complexity
    # l = r = 0 #max height in left and right
    # maxL = [0] * len(height) #list to save maxL[i] = the max height in the left in pos i
    # maxR = [0] * len(height) #list to save max[R] = the max height in the right in pos i
    # for i in range(len(height)):
    #     j = len(height) - 1 - i #index that moves from right to left in the list
    #     maxL[i] = l #we save the max height find from start to pos i-1
    #     maxR[j] = r #we save the max height find from the end to pos j+1
    #     l = max(l, height[i])
    #     r = max(r, height[j])
    # res = 0
    # for i in range(len(height)):
    #     pot = min(maxL[i], maxR[i])
    #     res += max(0, pot - height[i]) #pot - height[i]: the potencial wather minus the actual height
    # return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]
input()
print(trap(height))