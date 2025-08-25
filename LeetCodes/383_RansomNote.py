# Given two strings ransomNote and magazine, return true if ransomNote 
# can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
def canConstruct(ransomNote: str, magazine: str) -> bool:
    aux = {} #dictionary or hash table
    #add the letters available of magazine to our hash table
    for char in magazine:
        #get() is a method that take 2 params, (char) is the key to find, (0) defualt value if key don't exist
        aux[char] = aux.get(char, 0) + 1

    for char in ransomNote: #check if we can to build ransomNote from our hash table
        if char not in aux or aux[char] == 0: #check if the letter exist in aux |or| we use all the occurrences of this letter
            return False
        aux[char] -= 1
    return True



newRansomNote = "aa"
newMagazine = "ab"
input()
print(canConstruct(newRansomNote, newMagazine))