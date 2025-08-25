def twoSum(arr: list[int], target: int) -> bool:
    arr.sort() #sort the arr
    l, r = 0, len(arr) - 1

    while l < r:
        sum = arr[l] + arr[r]
        if sum == target:
            return True
        elif sum < target:
            l += 1
        else:
            r -= 1

    return False


arr = [10, -2, 19, 7, 9, 14]
target = 24
print(twoSum(arr, target))