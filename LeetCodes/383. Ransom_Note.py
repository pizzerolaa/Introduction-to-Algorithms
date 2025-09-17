# Given two strings ransomNote and magazine, return true if ransomNote can 
# be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

def ransom_note(ransomNote: str, magazine: str) -> bool:
    aux = {}
    for char in magazine:
        aux[char] = aux.get(char, 0) + 1

    for char in ransomNote:
        if char not in aux or aux[char] == 0:
            return False
        aux[char] -= 1

    return True

ransomNote = "aa"
magazine = "aab"
input()
print(ransom_note(ransomNote, magazine))

#another good solution but this dont use hash map and for interviews isnt good
# for letter in ransomNote:
#      if letter in magazine:
#          magazine = magazine.replace(letter, "", 1)
#      else:
#          return False
# return True