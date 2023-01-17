# https://www.python-lernen.de/while-schleife.htm
# https://www.python-lernen.de/uebung-zahlenraten.htm

"""schleife in Epoche einfügen mit 'soll ich weiter machen?'
   -> muss nicht mit Epoche sein, hauptsache input drin"""

"""mit 
durchgang = 0
aktiv = True
while aktiv:
    print(durchgang)
    durchgang = durchgang + 1
    if (durchgang == 3):
        aktiv = False
print("nach der Schleife")"""

def epochen():
    Jahr = int(input("Bitte Jahr eingeben \n"))

    if weitermachen == "weiter":
        print("ok, weiter geht es!")
        epochen()
    else:
        print("ok, tschüss")

    if Jahr < 0:
        print("vor Christus")

    elif 0 < Jahr <= 500:
        print("mit Christus")

    elif 500 < Jahr <= 750:
        print("frühes Mittelalter")

    elif 750 < Jahr <= 1250:
        print("hohes Mittelalter")

    elif 1250 < Jahr <= 1500:
        print("spätes Mittelalter")

    elif 1500 < Jahr <= 1600:
        print("Neuzeit")

    else:
        print("Bitte eine Zahl zwischen 0 und 1600 eingeben!")

durchgang = 0
aktiv = True
while aktiv:
    #print(durchgang)
    durchgang = durchgang + 1
    weitermachen = input("soll ich weitermachen? Ja/Nein \n")
    if weitermachen != "Ja":
        aktiv = False
    else:
        print("ok, tschüss")
#print("nach der Schleife")

#Zahlenratespiel