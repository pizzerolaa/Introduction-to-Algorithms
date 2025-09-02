# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

def check_valid(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    req = range(1, n + 1)
    for i in range(n):
        s = set()
        for j in range(n):
            item = matrix[i][j]
            if item in s:
                return False
            elif item != req:
                s.add(item)
    
    for i in range(n):
        s = set()
        for j in range(n):
            item = matrix[j][i]
            if item in s:
                return False
            elif item != req:
                s.add(item)
    
    return True

matrix = [[1,2,3],[3,1,2],[2,3,1]]
input()
print(check_valid(matrix=matrix))