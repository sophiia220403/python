import random

anzWurf = int(input("Bitte die Anzahl der Würfe eingeben: \n"))

results = [0, 0, 0, 0, 0, 0]

for i in range(anzWurf):
    roll = random.randint(1, 6)
    results[roll - 1] += 1

print("Ergebnisse der Simulation:\n")
for i in range(6):
    print("Zahl", i+1, "wurde ", results[i], "mal gewürfelt!")
