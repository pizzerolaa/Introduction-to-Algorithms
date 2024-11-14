# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

def reverseString(s: list[str]) -> list[str]:
    #this is the most easy solution, but i need make it without modifying the input array
    # s.reverse()
    # return s

    #this solution meets with the requeriments, as you can see we use the Two Pointers technique, 
    #this make this solution a O(n) time complexity
    l, r = 0, len(s) - 1
    while l <= r: #while left <= right we swap these variables using a temp var.
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        l += 1
        r -= 1
    
    return s

s = ["h","e","l","l","o"]
input()
print(reverseString(s))

