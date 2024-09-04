def romanToInt(s: str) -> int:
    dic = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
    convStrtoInt = [dic[char] for char in s if char in dic]
    conv = 0
    for i in range(len(convStrtoInt)- 1):
        if convStrtoInt[i] < convStrtoInt[i+1]:
            conv -= convStrtoInt[i]
        else:
            conv += convStrtoInt[i]
    conv += convStrtoInt[-1]
    return conv

st = input(str)
print(romanToInt(st))