import random

inp = int(input("Bitte eine Zahl eingeben \n"))
zufall = random.randint(1, 10)
while inp != zufall:
    print(f"{zufall} war die Zufallszahl")
    inp = int(input("Bitte eine neue Zahl eingeben \n"))
    zufall = random.randint(1, 10)

print(f"Zahl {inp} war richtig!")
