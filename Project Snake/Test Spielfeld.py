# Spielfeld/figuren zeichnen
spielfeld = [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]]

for yPos in range(len(spielfeld)):
    for xPos in range(len(spielfeld[0])):
        print(f"yPos = {yPos}, xPos = {xPos}: {spielfeld[yPos][xPos]}")
        # xPos = 0, yPos = 0 -> 0,0
        # xPos = 1, yPos = 0 -> 100, 0
        # xPos = 0, yPos = 1 ->  0, 100
        # xPos = 2, yPos = 0 -> 200, 0
        if spielfeld[yPos][xPos] == 1:
            pygame.draw.rect(screen, ROT, [xPos * 100, yPos * 100, 100, 100], 0)
        else:
            pygame.draw.rect(screen, ORANGE, [xPos * 100, yPos * 100, 100, 100], 0)
# 1: rect(0, 0, 100, 100)
# 2: rect(100, 0, 100, 100)
# 3: rect(200, 0, 100, 100)
# 4: rect(0, 100, 100, 100)