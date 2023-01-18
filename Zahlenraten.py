import random

#Durchgang und ZUfallszahl wird festgelegt
durchgang = 0
zufallszahl = random.randint(0, 99)

#Header
print("\n")
print("Sie haben 7 Versuche um die Zahl zu erraten. Viel Glück")
print(f"Durchgang: {durchgang}")
benutzereingabe = int(input("-> Bitte eine Zahl zwischen 1 - 100 eingeben \n"))


#Schleife
aktiv = True
while durchgang < 7:

    if benutzereingabe < zufallszahl:
        print("deine geratene Zahl ist zu klein")
        durchgang = durchgang + 1
        print(f"Durchgang: {durchgang}")
        benutzereingabe = int(input("Bitte eine Zahl zwischen 1 - 100 eingeben \n"))


    elif benutzereingabe > zufallszahl:
        print("deine geratene Zahl ist zu groß")
        durchgang = durchgang + 1
        print(f"Durchgang: {durchgang}")
        benutzereingabe = int(input("Bitte eine Zahl zwischen 1 - 100 eingeben \n"))

    elif benutzereingabe == zufallszahl:
        print("Gewonnen! :)")
        aktiv = False
        #Ausgabe = "Gewonnen" ohne Stop -> warum alles andere einmalig?

    elif benutzereingabe == "Ende" or benutzereingabe == "ende":
        print("ok, tschüss :(")
        aktiv = False
        #Probleme wegen int(), geht auch nicht mit "or" -> wie String und int in einer Eingabe?

    else:
        print("Eingabe ist nicht gültig")
        benutzereingabe = int(input("Bitte eine Zahl zwischen 1 - 100 eingeben \n"))

if durchgang >= 7:
    print("Du hast alle Versuche aufgebraucht.\nVersuche es doch nochmal!")
    aktiv = False




"""Probleme: 
    -durchgang anzeigen? ----
    -warum gewonnen so oft?
    -nach 7, durchgang abbrechen? ----
    -Ende als Eingabe?
"""



