import random as rand


def generatePassword(len):
    password = ""
    for x in range(0, len):
        val = rand.randint(33, 126)
        charOut = chr(val)
        password += charOut
    print(password)


length = int(input("Define password length in characters: \n"))
generatePassword(length)

