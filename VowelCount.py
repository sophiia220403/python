#vowels = ["a", "e", "i", "o", "u"]

benutzereingabe = input("Bitte Wort eingeben\n")
count = [0, 0, 0, 0, 0]
count[0] = "a"
count[1] = "e"
count[2] = "i"
count[3] = "o"
count[4] = "u"

def getcount(count):
    for i in benutzereingabe:
        count[i] += 1

print("Ergebnisse: \n")
for i in range(len(benutzereingabe)):
    print("Vokal" + count[i] + "wurde" + getcount(count) + "mal gezählt" )

"""
Idee: Wörter eingeben und in den Wörtern die Vokale zählen und in einer Liste ausspucken.

1. Liste erstellen, die den Anfangswert 0 hat und bei jedem gezählten Vokal eins hoch geht.
2. Listenposition einem Vokal zuordnen.
3. getCount so definieren, dass das Wort untersucht und die Vokale gezählt werden.
4. für jedes getCount den Wert der jeweiligen Listenposition um eins erhöhen, speichern.
5. Liste ausgeben.
6. Vllt mehrere Wörter auf einmal???
"""
