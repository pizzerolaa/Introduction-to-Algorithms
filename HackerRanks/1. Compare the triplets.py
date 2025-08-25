# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a: list[int], b: list[int]) -> list[int]:
    x = 0
    y = 0
    # Write your code here
    for i in range(len(a)):
        if a[i] > b[i]:
            x += 1
        elif a[i] < b[i]:
            y += 1
        else:
            x += 0
            y += 0
    return [x, y]

a = [1, 2, 3]
b = [3, 2, 1]
c = input(int)
print(compareTriplets(a, b))