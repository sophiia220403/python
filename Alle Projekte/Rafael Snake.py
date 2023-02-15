import pygame
import random
pygame.init()

hellgrau = ( 211, 211, 211)
schwarz = ( 0, 0, 0)
gruen = ( 173, 255, 47)
rot = ( 220, 20, 60)
gelb = ( 255, 255, 0)
weiss = ( 255, 255, 255)
xScreen = 1000
yScreen = 500
xSnake = 100
ySnake = 250
xSnakeChange = 0
ySnakeChange = 0
snakeLänge = 50
xFutter = 700
yFutter = 250
futterD = 15
spielAktiv = True

screen = pygame.display.set_mode((xScreen, yScreen))
pygame.display.set_caption("Für die alten Säcke unter euch: Snake!")

clock = pygame.time.Clock()

while spielAktiv:
    # Snakebewegung
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielAktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xSnakeChange = 10
                ySnakeChange = 0
            elif event.key == pygame.K_UP:
                xSnakeChange = 0
                ySnakeChange = -10
            elif event.key == pygame.K_LEFT:
                xSnakeChange = -10
                ySnakeChange = 0
            elif event.key == pygame.K_DOWN:
                xSnakeChange = 0
                ySnakeChange = 10
    xSnake += xSnakeChange
    ySnake += ySnakeChange

    screen.fill(hellgrau)
    snake = pygame.draw.rect(screen, gruen, [xSnake, ySnake, snakeLänge, 15])
    snakeKopf = pygame.draw.ellipse(screen, gruen, [xSnake + snakeLänge, ySnake, futterD, futterD])
    futter = pygame.draw.ellipse(screen, rot, [xFutter, yFutter, futterD, futterD])

    if snakeKopf.colliderect(futter):
        xFutter = random.randint(0 + futterD, xScreen - futterD)
        yFutter = random.randint(0 + futterD, yScreen - futterD)
        snakeLänge += 50


    if xSnake >= 1000 or xSnake < 0 or ySnake >= 500 or ySnake < 0:
        spielAktiv = False



    pygame.display.flip()
    clock.tick(25)


pygame.quit()