"""Write a while loop that adds all the numbers up to 100 (inclusive).
Code snippet"""

counter=0
total=0

aktiv = True
while aktiv:
    total = total + counter

    counter = counter +1
    if counter == 101:
        aktiv = False




print(total)



