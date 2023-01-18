#bis 100 Zählen lassen
def bis100Zaehlen():
    counter = -1
    aktiv = True
    while aktiv:
        counter = counter +1
        if counter == 100:
            aktiv = False

        print(counter)

bis100Zaehlen()

#bis 100 Zählen lassen, aber in 2er Schritten
def bis100Alle2Zaehlen():

    for Zahl in range(0, 101, 2):
        print(Zahl)

    print()

bis100Alle2Zaehlen()

