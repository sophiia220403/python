import pygame
from pygame.locals import *

pygame.init()

Mensch = [" ", " ", " ", " "]

Mensch[0] = pygame.image.load("1.png")
Mensch[1] = pygame.image.load("2.png")
Mensch[2] = pygame.image.load("3.png")
Mensch[3] = pygame.image.load("4.png")

lila = (204, 169, 221)

frame = 0

fenster = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Mensch animieren")
clock = pygame.time.Clock()

spielaktiv = True

while spielaktiv:
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            spielaktiv = False

    fenster.fill(lila)

    frame += 1

    if frame > 3:
        frame = 0

    fenster.blit(Mensch[frame], (100, 100))

    pygame.display.flip()
    clock.tick(7)

pygame.quit()
