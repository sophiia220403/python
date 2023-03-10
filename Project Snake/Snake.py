import pygame
import random
import math
import sys


# Genutze Farben
ORANGE = (255, 140, 0)
ROT = (255, 105, 97)
GRUEN = (0, 130, 10)
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)
GRAU = (211, 211, 211)
BGGRUEN = (73, 182, 117)


# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

FENSTERBREITE = 400
FENSTERHOEHE = 300

screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))
# Titel für Fensterkopf
pygame.display.set_caption("Snake")
pygame.init()


def game():
    #Score
    score = 0
    anzKoerper = 1

    #Highscore
    datei = open("Highscore", "r", encoding="utf-8")
    Highscore = int(datei.read())

    # solange die Variable True ist, soll das Spiel laufen
    ProgrammAktiv = True

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

    #SnakeKopf Rechteck erstellen
    #rect = pygame.draw.rect(screen, GRAU, [snakepos_x, snakepos_y - 16, 20, 37])


    # Schleife Hauptprogramm
    while ProgrammAktiv:
        # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print("Spieler hat Quit-Button angeklickt")
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                ProgrammAktiv = False
                break
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
            anzKoerper += 1
            bewegungsTemp += 0.1

        #Highscore erhöhen
        if Highscore < score:
            Highscore = score
            datei.write(score)

            datei.close()

        # Spielfeld löschen
        screen.fill(SCHWARZ)

        # Spielfeld/figuren zeichnen
        #screen.fill(BGGRUEN)
        screen.fill(GRAU)
        pygame.draw.rect(screen, SCHWARZ, [0, 0, 400, 300], 3)

        #Rechteck um Schlangenkopf
        #!    pygame.transform.rotate(rect, 90)

        #Schlangenkopf
        pygame.draw.rect(screen, GRUEN, [snakepos_x, snakepos_y, ApfelBreite, ApfelHoehe])

        #weiße Augen
        pygame.draw.ellipse(screen, WEISS, [snakepos_x, snakepos_y, 9, 9])
        pygame.draw.ellipse(screen, WEISS, [snakepos_x + 11, snakepos_y, 9, 9])

        #schwarze Pupillen
        pygame.draw.ellipse(screen, SCHWARZ, [snakepos_x + 2, snakepos_y - 1 + 3, 4, 4])
        pygame.draw.ellipse(screen, SCHWARZ, [snakepos_x + 14, snakepos_y - 1 + 3, 4, 4])

        #Zunge
        pygame.draw.rect(screen, ROT, [snakepos_x + 8, snakepos_y - 15, 3, 15])

        pygame.Surface.blit(screen, Apfel, (Apfel_x, Apfel_y))

        #Bewegung Snake
        snakepos_x += bewegung_x
        snakepos_y += bewegung_y

        #Game Over bei Wand
        if snakepos_y > FENSTERHOEHE - SNAKE_DURCHMESSER or snakepos_y < 0:
            endscreen(score)

        if snakepos_x > FENSTERBREITE - SNAKE_DURCHMESSER or snakepos_x < 0:
            endscreen(score)

        #Fenster aktualisieren
        pygame.display.flip()
        # Refresh-Zeiten festlegen
        clock.tick(60)
    game()


def endscreen(score):
    font = pygame.font.SysFont(None, 40)
    font2 = pygame.font.SysFont(None, 30)
    agn = font2.render(f"Nochmal?", True, SCHWARZ)
    ext = font2.render(f"Beenden", True, SCHWARZ)
    esc = font.render(f"'esc'", True, SCHWARZ)
    q = font.render(f"'q'", True, SCHWARZ)
#Endscreen
    screen.fill(ROT)
    pygame.draw.rect(screen, SCHWARZ, [0, 0, 400, 300], 3)
    img = font.render(f"Punkte: {score}", True, SCHWARZ)
    screen.blit(img, (132, 70))
    screen.blit(agn, (60, 170))
    screen.blit(ext, (240, 170))
    screen.blit(esc, (255, 210))
    screen.blit(q, (90, 210))

game()
endscreen()


pygame.quit()

"""
1. Schlange verlängern + aneinander (Liste, jedes Element aus Tripel(x, y, Richtung) 
2. Highscore (evtl auch abspeichern in extra Datei)
3. Schlange verschönern + animieren
6. BLocken, dass Schlange sich nicht um 180 Grad drehen kann
8. Variable die schaut, ob ich in game oder screen bin -> muss mit spielaktiv arbeiten, wenn True = im Game, 
   wenn False = im Screen
9. Spielfeld schön machen mit Kacheln zeichnen
"""


"""
Probleme:
3. Wie verlängere ich die Schlange?
4. End Screen kann verlassen werden wenn Snake wieder in Bildshirm"""