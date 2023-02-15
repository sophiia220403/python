liste = [1, 2, 3, 4, 5]

print(f"aktuelle Liste: {liste}")
benutzereingabe = int(input("Bitte eine Zahl eingeben\n"))
schleifeaktiv = True


while schleifeaktiv:
    liste.append(benutzereingabe)
    del liste[0]
    def AverageList(liste):
        return sum(liste) / len(liste)

   # if len(liste) == len(converted):
    #    print("Keine doppelten Einträge")
    #else:
     #   if set[0] == liste[0]:

    converted = set(liste)

    def doppelt():
        if converted[0] == liste[0]:
            ???

    print(converted)
    print(liste)
    print(f"Der Durchschnitt ist: {AverageList(liste)}")
    print(f"Die größte Zahl der Liste ist: {max(liste)}")
    #print(get_dups(liste))

    benutzereingabe = int(input("Bitte eine Zahl eingeben\n"))


"""
in Sets umwandeln
mit liste vergleichen
oder
sortierter liste und dann doppelte werte raussuchen
"""