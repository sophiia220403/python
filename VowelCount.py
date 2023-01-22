#vowels = ["a", "e", "i", "o", "u"]

benutzereingabe = input("Bitte Wort eingeben\n")

def getVowels():
    numVowels = 0
    for i in benutzereingabe:
        if i in ["a", "e", "i", "o", "u"]:
            numVowels = numVowels + 1

        else:
            pass

print(getVowels())