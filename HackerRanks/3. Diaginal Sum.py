# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
def diagonalDiference(matrix: list[list[int]]) -> int:
    fd, ld = 0, 0
    for i in range(len(matrix)):
        fd += matrix[i][i]
        ld += matrix[i][-i-1]

    return abs(fd - ld)

matrix = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
input()
print(diagonalDiference(matrix))