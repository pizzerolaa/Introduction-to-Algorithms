# You're given strings jewels representing the types of stones that are jewels, and stones 
# representing the stones you have. Each character in stones is a type of stone you have. 
# You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

def numJewelsInStones(jewels: str, stones: str) -> int:
    #This is my solution, the complexity is O(N+M), meh, but the next comment have a better complex
    convert = set(jewels)
    count = 0
    for i in range(len(stones)):
        if convert.intersection(stones[i]):
            count += 1
    return count

    #Random solution
    # aux = set(jewels)
    # return sum((1 for x in stones if x in aux))

newJewels = "aA"
newStones = "aAAbbbb"
input()
print(numJewelsInStones(newJewels, newStones))