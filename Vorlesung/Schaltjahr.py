

def Schaltjahr():


    aktiv = True
    while aktiv:
        eingabeJahr = int(input("Bitte Jahreszahl eingeben \n"))

        if (0 == (eingabeJahr % 4) and 0 != (eingabeJahr % 100)) or 0 == (eingabeJahr % 400):
            print("Schaltjahr")
        else:
            print("kein Schaltjahr")

        weitermachen = input("Soll ich weitermachen? Ja / Nein \n")

        if weitermachen == "Ja" or weitermachen == "ja":
            print("")
        else:
            print("ok, tschüss")
            aktiv = False


Schaltjahr()