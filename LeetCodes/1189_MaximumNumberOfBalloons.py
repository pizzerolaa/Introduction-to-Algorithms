# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

def maxNumberofBallons(text: str) -> int:
    aux = {}

    for char in text:
        aux[char] = aux.get(char, 0) + 1

    if not all(char in aux for char in "balloon"):
        return 0
    
    return min( #hell nah lil bro, we count the min cant of letters in aux(dict)
        aux.get('b', 0),
        aux.get('a', 0),
        aux.get('l', 0) // 2,
        aux.get('o', 0) // 2,
        aux.get('n', 0)
    )

newText = "loonbalxballpoon"
input()
print(maxNumberofBallons(newText))
