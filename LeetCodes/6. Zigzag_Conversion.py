# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows 
# like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int num_rows);

def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return(s)
    res = [[] for _ in range(num_rows)]
    row = 0
    direc = -1
    for char in s:
        res[row].append(char)
        if row == 0 or row == num_rows - 1:
            direc *= -1
        row += direc
    return "".join("".join(row) for row in res)

s = "PAYPALISHIRING"
num_rows = 3
input()
print(convert(s, num_rows))