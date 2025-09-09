# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

# Given an integer n, return a list of two integers [a, b] where:
# a and b are No-Zero integers.
# a + b = n

# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

def get_no_zero_integers(n: int) -> list[int]:
    a, b = n - 1, 1
    while '0' in str(a) or '0' in str(b):
        b += 1
        a = n - b
    return [a, b]

n = 11
input()
print(get_no_zero_integers(n))

#for loop solution:
# def get_no_zero_integers(n: int) -> list[int]:
#     for i in range(1, n):
#         a = i
#         b = n - i
#         if a > 0 and b > 0 and '0' not in str(a) and '0' not in str(b):
#             res = [a, b]
#     return res