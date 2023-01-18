import random

inp = int(input("Bitte eine Zahl eingeben \n")) % 10

zufall = random.randint(1, 10)
while inp != zufall:
    print(zufall)
    zufall = random.randint(1, 9)
print(f"Zahl {inp} erreicht.")