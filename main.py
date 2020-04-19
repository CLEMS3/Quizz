# Clément Chapard - QuizzNsi
# main file of the project

# importation of modules
import pygame
import csv
import os
import Soundex

# window initialization
pygame.init()

# images importation
def importation(image_name):
    return pygame.image.load(str(image_name))

bg = importation("src/menu_bg.png")
tr = importation("src/Trophy.png")
lg = importation("src/Statistics.png")


# window setting
win = pygame.display.set_mode((1000, 600))
win.blit(bg, (0, 0))

# main loop
_continue = True
while _continue:
    for i in pygame.event.get():
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE] or i.type == pygame.QUIT:
            pygame.quit()
            os.sys.exit(0)
    pygame.display.flip()
