# Given a string text, you want to use the characters of text to form 
# as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.
from collections import Counter

def max_num_balloons(text: str) -> int:
    letter = 'balloon'
    hmap = {}

    for char in text:
        hmap[char] = hmap.get(char, 0) + 1

    count = 0
    while True:
        for char in letter:
            if hmap.get(char, 0) == 0:
                return count
            hmap[char] -= 1
        count += 1

text = "nlaebolko"
input()
print(max_num_balloons(text))

#best solution my nigg:
# def max_num_balloons(text: str) -> int:
#     count = Counter(text)
#     letter = Counter("balloon")
#     return min(count[c] // letter[c] for c in letter)

#firts solution
# def maxNumberofBallons(text: str) -> int:
#     aux = {}

#     for char in text:
#         aux[char] = aux.get(char, 0) + 1

#     if not all(char in aux for char in "balloon"):
#         return 0
    
#     return min( #hell nah lil bro, we count the min cant of letters in aux(dict)
#         aux.get('b', 0),
#         aux.get('a', 0),
#         aux.get('l', 0) // 2,
#         aux.get('o', 0) // 2,
#         aux.get('n', 0)
#     )