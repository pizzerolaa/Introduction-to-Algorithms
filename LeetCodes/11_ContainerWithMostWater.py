# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints 
# of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

def maxArea(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    count = 0
    while l < r:
        width = r - l
        h = min(height[l], height[r])
        area = width * h
        count = max(count, area)
        if height[l] < height[r]:
            l+= 1
        else:
            r -= 1

    return count

height = [1,8,6,2,5,4,8,3,7]
input()
print(maxArea(height))