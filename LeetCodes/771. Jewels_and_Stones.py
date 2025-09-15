# You're given strings jewels representing the types of stones that are jewels, and stones 
# representing the stones you have. Each character in stones is a type of stone you have. 
# You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

def num_jewels_in_stones(jewels: str, stones: str) -> int:
    aux = set(jewels)
    return sum(1 for char in stones if char in aux)

jewels = "aA"
stones = "aAAbbbb"
input()
print(num_jewels_in_stones(jewels, stones))

#my solution but the time complex is O(len(jewels)) or O(N + M)
# def num_jewels_in_stones(jewels: str, stones: str) -> int:
#     res = {}
#     for char in stones:
#         if char in jewels:
#             res[char] = res.get(char, 0) + 1
#     return sum(res.values())

#This is my solution, the complexity is O(N+M), meh, but the next comment have a better complex
# def numJewelsInStones(jewels: str, stones: str) -> int:
#     convert = set(jewels)
#     count = 0
#     for i in range(len(stones)):
#         if convert.intersection(stones[i]):
#             count += 1
#     return count