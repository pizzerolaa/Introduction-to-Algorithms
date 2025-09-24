# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    # Each row must contain the digits 1-9 without repetition.
    # Each column must contain the digits 1-9 without repetition.
    # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
    # A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    # Only the filled cells need to be validated according to the mentioned rules.

def is_valid_sudoku(board: list[list[str]]) -> bool:
    if len(board) != 9 or any(len(row) != 9 for row in board):
        return False

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            #validar caracter
            if val < '1' or val > '9':
                return False
            b = (r // 3) * 3 + (c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[b]:
                return False
            rows[r].add(val)
            cols[c].add(val)
            boxes[b].add(val)
    return True


board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

input()
print(is_valid_sudoku(board=board))

#first solution, well the second one but with good time and space
# def is_valid_sudoku(board: list[list[str]]) -> bool:
#     #validate rows
#     for i in range(9):
#         s = set()
#         for j in range(9):
#             item = board[i][j]
#             if item in s:
#                 return False
#             elif item != '.':
#                 s.add(item)

#     #validate colums
#     for i in range(9):
#         s = set()
#         for j in range(9):
#             item = board[j][i]
#             if item in s:
#                 return False
#             elif item != '.':
#                 s.add(item)

#     #validate boxes
#     starts = [(0, 0), (0, 3), (0,6),
#               (3, 0), (3, 3), (3, 6),
#               (6, 0), (6, 3), (6, 6)]
    
#     for i, j in starts:
#         s = set()
#         for row in range(i, i + 3):
#             for col in range(j, j + 3):
#                 item = board[row][col]
#                 if item in s:
#                     return False
#                 elif item != '.':
#                     s.add(item)
#     return True