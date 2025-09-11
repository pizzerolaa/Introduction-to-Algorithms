# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should 
# be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    a = m - 1
    b = n - 1
    c = m + n - 1

    while a >= 0 and b >= 0:
        if nums1[a] < nums2[b]:
            nums1[c] = nums2[b]
            b -= 1
        else:
            nums1[c] = nums1[a]
            a -= 1
        c -= 1
    
    while b >= 0:
        nums1[c] = nums2[b]
        b -= 1
        c -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
input()
print(merge(nums1, m, nums2, n))

#another solution:
# for i in range(m, m + n):
#     nums1[i] = nums2[i - m]
# nums1.sort()