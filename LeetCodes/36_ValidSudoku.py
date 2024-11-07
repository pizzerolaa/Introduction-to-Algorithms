# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
def isValidSudoku(board:list[list[int]]) -> bool:
    #validate rows
    for row in range(9):
        aux = set()
        for cols in range(9):
            item = board[row][cols]
            if item in aux:
                return False
            elif item != '.':
                aux.add(item)

    #validate cols
    for row in range(9):
        aux = set()
        for cols in range(9):
            item = board[cols][row]
            if item in aux:
                return False
            elif item != '.':
                aux.add(item)

    #validate boxes
    for row in range(0, 9, 3):
        for cols in range(0, 9, 3):
            aux = set()
            for i in range(3):
                for j in range(3):
                    if board[row+i][cols+j] in aux:
                        return False
                    elif board[row+i][cols+j] != '.':
                        aux.add(board[row+i][cols+j])
    
    return True


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
input()
print(isValidSudoku(board))