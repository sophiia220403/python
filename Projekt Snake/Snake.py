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

#Score
score = 0
anzKörper = 1


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

bewegung_x = 0
bewegung_y = 0

bewegungsTemp = 2.5
ApfelBreite = 20
ApfelHoehe = 20
Apfel = pygame.image.load("Apfel.png")
Apfel = pygame.transform.scale(Apfel, (ApfelBreite, ApfelHoehe))
Apfel_x = random.randint(0 + ApfelBreite + 5, FENSTERBREITE - ApfelBreite - 5)
Apfel_y = random.randint(0 + ApfelHoehe + 5, FENSTERHOEHE - ApfelHoehe - 5)


# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")

            # Taste für Spieler
            if event.key == pygame.K_RIGHT:
                print("Spieler hat Pfeiltaste rechts gedrückt")
                bewegung_x = 1 * bewegungsTemp
                bewegung_y = 0 * bewegungsTemp
            elif event.key == pygame.K_LEFT:
                print("Spieler hat Pfeiltaste links gedrückt")
                bewegung_x = -1 * bewegungsTemp
                bewegung_y = 0 * bewegungsTemp
            elif event.key == pygame.K_UP:
                print("Spieler hat Pfeiltaste hoch gedrückt")
                bewegung_x = 0 * bewegungsTemp
                bewegung_y = -1 * bewegungsTemp
            elif event.key == pygame.K_DOWN:
                print("Spieler hat Pfeiltaste runter gedrückt")
                bewegung_x = 0 * bewegungsTemp
                bewegung_y = 1 * bewegungsTemp

    #print(snake())


    # Spiellogik hier integrieren
    if abs(snakepos_x - Apfel_x) < ApfelBreite and abs(snakepos_y - Apfel_y) < ApfelHoehe:
        Apfel_x = random.randint(0 + ApfelBreite + 5, FENSTERBREITE - ApfelBreite - 5)
        Apfel_y = random.randint(0 + ApfelHoehe + 5, FENSTERHOEHE - ApfelHoehe - 5)
        score += 1
        anzKörper += 1

    # Spielfeld löschen
    screen.fill(SCHWARZ)

    # Spielfeld/figuren zeichnen
    screen.fill(GRAU)
    pygame.draw.rect(screen, SCHWARZ, [0, 0, 400, 300], 3)
    pygame.draw.ellipse(screen, GRUEN, [snakepos_x, snakepos_y, 20, 20])

    pygame.Surface.blit(screen, Apfel, (Apfel_x, Apfel_y))

    #Bewegung Snake
    snakepos_x += bewegung_x
    snakepos_y += bewegung_y

    #Game Over bei Wand
    if snakepos_y > FENSTERHOEHE - SNAKE_DURCHMESSER or snakepos_y < 0:
        spielaktiv = False

    if snakepos_x > FENSTERBREITE - SNAKE_DURCHMESSER or snakepos_x < 0:
        spielaktiv = False
    #Fenster aktualisieren
    pygame.display.flip()
    # Refresh-Zeiten festlegen
    clock.tick(60)


print(score)
pygame.quit()

"""
1. Schlange verlängern + aneinander (Liste, jedes Element aus Tripel(x, y, Richtung) 
2. Highscore (evtl auch abspeichern in extra Datei 
3. Schlange verschönern + animieren
4. """