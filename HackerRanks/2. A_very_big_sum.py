#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar: list[int]) -> int:
    # Write your code here
    return sum(ar)

ar = [1, 3, 5, 6, 9, 7, 7, 377, 1993]
print(aVeryBigSum(ar))