import random

anzPunkte = int(input("Bitte eine Zahl eingeben (mind. 100)"))
anzPunkteKreis = 0


for i in range(anzPunkte):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y <= 1:
        anzPunkteKreis += 1

pi = 4 * anzPunkteKreis / anzPunkte
print(pi)