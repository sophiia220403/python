import pygame


fenster = pygame.display.set_mode((400, 300))

clock = pygame.time.Clock()

WEISS = (255, 255, 255)
BLAU = (0, 0, 255)

open("Spielfeld", "r")
karte = open("Spielfeld", "r")
print(karte.read())

def element_zeichnen(spalte, reihe):
    pygame.draw.rect(fenster, BLAU)

for x in range(0, 8):
    for y in range(0, 9):
        if karte != 0:
            element_zeichnen(x, y)

pygame.quit()