# Clément Chapard - QuizzNsi
# main file of the project

# importation of modules
import pygame
import csv
import os
import Soundex


# window initialization
pygame.init()
win = pygame.display.set_mode((1000, 600))

# main loop
_continue = True
while _continue:
    for i in pygame.event.get():
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE] or i.type == pygame.QUIT:
            pygame.quit()
            os.sys.exit(0)


