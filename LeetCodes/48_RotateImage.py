# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

def rotate(matrix: list[list[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                  matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
        for i in range(len(matrix)):
              matrix[i].reverse()
    
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix1)
rotate(matrix2)
print(matrix2)




