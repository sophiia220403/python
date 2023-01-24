import random

spiel_aktiv = True
spieler_aktuell = 'X'

spielfeld = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " ",]

def spielfeld_ausgeben():
    print(spielfeld[0] + " |" + spielfeld[1] + " |" + spielfeld[2])
    print("--------")
    print(spielfeld[3] + " |" + spielfeld[4] + " |" + spielfeld[5])
    print("--------")
    print(spielfeld[6] + " |" + spielfeld[7] + " |" + spielfeld[8])

def spieler_eingabe():
    global spiel_aktiv
    while True:
        spielzug = input("Bitte Feld eingeben: \n")
        if spielzug == 'q':
            spiel_aktiv = False
            return
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Bitte Zahl von 1 bis 9 eingeben: \n")
        else:
            if spielzug >= 1 and spielzug <= 9:
                if spielfeld[spielzug] == "X" or spielfeld[spielzug] == "O":
                    print("Das Feld ist bereits belegt - ein anderes wählen!")
                else:
                    return spielzug
            else:
                print("Zahl muss zwischen 1 und 9 liegen! \n")

def spieler_wechseln():
    global spieler_aktuell
    if spieler_aktuell == 'X':
        spieler_aktuell = 'O'
    else:
        spieler_aktuell = 'X'



def kontrolle_gewonnen():
    #Reihen
    if spielfeld[0] == spielfeld[1] == spielfeld[2]:
        return spielfeld[0]
    if spielfeld[3] == spielfeld[4] == spielfeld[5]:
        return spielfeld[3]
    if spielfeld[6] == spielfeld[7] == spielfeld[8]:
        return spielfeld[6]
    #Spalten
    if spielfeld[0] == spielfeld[3] == spielfeld[6]:
        return spielfeld[0]
    if spielfeld[1] == spielfeld[4] == spielfeld[7]:
        return spielfeld[1]
    if spielfeld[2] == spielfeld[5] == spielfeld[8]:
        return spielfeld[2]
    #Diagonalen
    if spielfeld[0] == spielfeld[4] == spielfeld[8]:
        return spielfeld[4]
    if spielfeld[2] == spielfeld[4] == spielfeld[6]:
        return spielfeld[4]


def kontrolle_auf_untentschieden():
    if (spielfeld[0] == "X" or spielfeld[0] == "O") \
        and (spielfeld[1] == "X" or spielfeld[1] == "O") \
        and (spielfeld[2] == "X" or spielfeld[2] == "O") \
        and (spielfeld[3] == "X" or spielfeld[3] == "O") \
        and (spielfeld[4] == "X" or spielfeld[4] == "O") \
        and (spielfeld[5] == "X" or spielfeld[5] == "O") \
        and (spielfeld[6] == "X" or spielfeld[6] == "O") \
        and (spielfeld[7] == "X" or spielfeld[7] == "O") \
        and (spielfeld[8] == "X" or spielfeld[8] == "O"):
            return ("unentschieden")


spielfeld_ausgeben()
while spiel_aktiv:
    print()
    print ("Spieler " + spieler_aktuell + " am Zug")

    spielfeld_KI = []
    for moegliche_felder in spielfeld:
        if moegliche_felder != "X" and moegliche_felder != "O" and moegliche_felder != " ":
            spielfeld_KI += moegliche_felder

    if spieler_aktuell == "0":
        spielzug = int(random.choice(spielfeld_KI))
    else:
        spielzug = spieler_eingabe()

    spielzug = spieler_eingabe()
    if spielzug:
        spielfeld[spielzug] = spieler_aktuell
        spielfeld_ausgeben()
        gewonnen = kontrolle_gewonnen()
        if gewonnen:
            print("Spieler " + gewonnen + " hat gewonnen!")
            spiel_aktiv = False
        unentschieden = kontrolle_auf_untentschieden()
        if unentschieden:
            print("Das Spiel ist unentschieden ausgegangen!")
            spiel_aktiv = False
        spieler_wechseln()

print()