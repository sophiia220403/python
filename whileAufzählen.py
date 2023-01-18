vornamen = ["Axel", "Elke", "Martin"]

counter = -1

aktiv = True
while aktiv:
    counter = counter + 1
    if counter == (len(vornamen)-1):
        aktiv = False

    #print(counter)
    print(vornamen[counter])