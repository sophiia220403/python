firstQuarter = ["Januar", "Februar", "März"]
secondQuarter = ["April", "Mai", "Juni"]
thirdQuarter = ["Juli", "August", "September"]
forthQuarter = ["Oktober", "November", "Dezember"]

benutzereingabe = input("Bitte einen Monat eingeben\n")

if benutzereingabe in firstQuarter:
    print("1. Quartal")

elif benutzereingabe in secondQuarter:
    print("2. Quartal")

elif benutzereingabe in thirdQuarter:
    print("3. Quartal")

elif benutzereingabe in forthQuarter:
    print("4. Quartal")

else:
    print("Bitte eingabe erneut versuchen")
