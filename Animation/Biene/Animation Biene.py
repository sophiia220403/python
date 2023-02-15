

# Importieren u. initialisieren der Pygame-Bibliothek
import pygame
from pygame.locals import *
pygame.init()

# Variablen/KONSTANTEN setzen
W, H = 800, 600
FPS  = 30
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
GRAU    = ( 155, 155, 155)
spielaktiv = True

biene = ['','','','','','']
biene[0] = pygame.image.load("biene-r-001.png")
biene[1] = pygame.image.load("biene-r-002.png")
biene[2] = pygame.image.load("biene-r-003.png")
biene[3] = pygame.image.load("biene-r-004.png")
biene[4] = pygame.image.load("biene-r-005.png")
biene[5] = pygame.image.load("biene-r-006.png")

frame = 0

# Definieren und Öffnen eines neuen Fensters
fenster = pygame.display.set_mode((W, H))
pygame.display.set_caption("python-lernen.de - Sprite (mehrere Grafiken) animieren")
clock = pygame.time.Clock()

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        # Beenden bei [ESC] oder [X]
        if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            spielaktiv = False

    # Spiellogik

    # Spielfeld löschen
    fenster.fill(GRAU)

    # Spielfeld/figuren zeichnen
    frame += 1

    if frame > 5:
        frame = 0

    fenster.blit(biene[frame], (10, 10))

    # Fenster aktualisieren
    pygame.display.flip()
    clock.tick(FPS)