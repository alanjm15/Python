def is_anagram(str1, str2):
    charWord1 = []
    charWord2 = []
    matches = 0
    # check length. If they are not the same, obviously can't be an anagram
    if(len(str1) != len(str2)):
        print("Not the same length: Cannot be an anagram")
        return False
    # change strings into char array
    for x in range(0, len(str1)):
        charWord1.append(str1[x])
        charWord2.append(str2[x])
    # sort them to attempt to line up the characters
    charWord1.sort()
    charWord2.sort()

    print(charWord1)
    print(charWord2)
    # since they are sorted, if each letter matches the other words letters, it must be an anagram
    for x in range(0, len(charWord1)):
        if(charWord1[x] == charWord2[x]):
            matches = matches + 1
    #matches should be the same number as the length of either of the words
    if(matches == len(word1)):
        print("Characters match. It is an anagram")
        return True
    else:
        print("Characters do not match. It is not an anagram")
        return False


    
          
word1 = "parted"
word2 = "lasted"

print(is_anagram(word1, word2))

print()

word1 = "alan"
word2 = "nala"

print(is_anagram(word1, word2))

