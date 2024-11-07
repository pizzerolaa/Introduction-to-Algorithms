# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.

def plusMinus(arr: list[int]):
    z, p, m = 0, 0, 0
    for num in arr:
        if num < 0:
            m += 1
        elif num > 0:
            p += 1
        else:
            z += 1
            
    z, p, m = map(lambda x: round(x / len(arr), 5), (z, p, m))

    return z, p, m

arr = [-4, 3, -9, 0, 4, 1]
print(plusMinus(arr))