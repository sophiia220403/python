import pygame
import random
import math


pygame.init()

#Genutze Farben
ORANGE = (255, 140, 0)
ROT = (255, 0, 0)
GRUEN = (0, 130, 10)
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)
GRAU = (211, 211, 211)


#Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

FENSTERBREITE = 400
FENSTERHOEHE = 300
# Fenster öffnen
screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))

# Titel für Fensterkopf
pygame.display.set_caption("Snake")

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

#Snake erstellen
"""def snake():
    #pygame.draw.arc(screen,SCHWARZ,[200,150,10,10], 0, math.pi, 1)
    pygame.draw.rect(screen, SCHWARZ, [200, 150, 10, 10], 0)
    pygame.draw.rect(screen, SCHWARZ, [200, 160, 10, 10], 0)
    pygame.display.update()"""

snakepos_x = 195
snakepos_y = 145

SNAKE_DURCHMESSER = 20

bewegung_x = 4
bewegung_y = 4

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")

            # Taste für Spieler 1
            if event.key == pygame.K_RIGHT:
                print("Spieler hat Pfeiltaste rechts gedrückt")
            elif event.key == pygame.K_LEFT:
                print("Spieler hat Pfeiltaste links gedrückt")
            elif event.key == pygame.K_UP:
                print("Spieler hat Pfeiltaste hoch gedrückt")
            elif event.key == pygame.K_DOWN:
                print("Spieler hat Pfeiltaste runter gedrückt")
            elif event.key == pygame.K_SPACE:
                print("Spieler hat Leertaste gedrückt")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Spieler hast Maus angeklickt")
    #print(snake())


    # Spiellogik hier integrieren

    # Spielfeld löschen
    screen.fill(SCHWARZ)

    # Spielfeld/figuren zeichnen
    screen.fill(GRAU)
    pygame.draw.rect(screen, SCHWARZ, [0, 0, 400, 300], 3)
    pygame.draw.ellipse(screen, GRUEN, [snakepos_x, snakepos_y, 20, 20])

    #Bewegung Snake
    snakepos_x += bewegung_x
    snakepos_y += bewegung_y

    if snakepos_y > FENSTERHOEHE - SNAKE_DURCHMESSER or snakepos_y < 0:
        bewegung_y = bewegung_y * -1

    if snakepos_x > FENSTERBREITE - SNAKE_DURCHMESSER or snakepos_x < 0:
        bewegung_x = bewegung_x * -1
    #Fenster aktualisieren
    pygame.display.flip()
    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()