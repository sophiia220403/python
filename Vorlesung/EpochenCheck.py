#def epochen(): -> damit alles richtig eingerückt ist, was dazu gehört

Jahr = int(input("Bitte Jahr eingeben \n"))

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


"""if__name__ == 'main':
    epochen()"""