# Given an m x n matrix, rettrn all elements of the matrix in spiral order.

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    #the complexity of this is O(m*n)
    res = []
    m, n = len(matrix), len(matrix[0]) #num of rows and columns
    i, j = 0, 0 #actual index for row and column
    t, r, b, l = 0, 1, 2, 3 #walls or boundarys for not exceed the limit on the matrix
    dir = r #direction of the movement

    #actual values for the walls
    tw = 0
    rw = n
    bw = m
    lw = -1

    while len(res) != m*n:
        #if direction is right the current row is traversed from left to right and each element is added to 'res'. 
        # Then it moves to the next row (incrementing 'i') and updates the right wall 'rw' (decreasing the width from the right)
        if dir == r: 
            while j < rw: 
                res.append(matrix[i][j])
                j += 1
            i, j = i + 1, j - 1
            rw -= 1
            dir = b
        #if direction is down the current column is traversed for top to bottom and each element is added to 'res'. 
        # Then it moves to the next column (decrementing 'j') and updates the bottom wall (decrementing the height at the bottom) 
        elif dir == b:
            while i < bw:
                res.append(matrix[i][j])
                i += 1
            i, j = i - 1, j - 1
            bw -= 1
            dir = l
        #if direction is left the current row is traversed for right to left and each element is added to 'res'. 
        # Then it moves to the next row (decreasing 'i') and updates the left wall (incrementing the left edge)
        elif dir == l:
            while j > lw:
                res.append(matrix[i][j])
                j -= 1
            i, j = i - 1, j + 1
            lw += 1
            dir = t
        # if direction is top the current column is traversed for bottom to top and each element is added to 'res'. 
        # Then it moves to the next column (increasing 'i') and updates the top wall (incrementing top edge)
        else:
            while i > tw:
                res.append(matrix[i][j])
                i -= 1
            i, j = i + 1, j + 1
            tw += 1
            dir = r
    return res 

matrix = [[1,2,3],[4,5,6],[7,8,9]]
input()
print(spiralOrder(matrix))