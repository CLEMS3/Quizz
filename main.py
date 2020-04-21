# Clément Chapard - QuizzNsi
# main file of the project

# importation of modules
import pygame
import csv
import os
import Soundex
from Views import *

# window initialization
pygame.init()


# images importation
def importation(image_name):
    return pygame.image.load(str(image_name))


def conv_icone_size(image):
    return pygame.transform.scale(image, (50, 50))


lang = "fr"
bg_main_menu_img = importation("src/menu_bg.png")
tr_img = conv_icone_size(importation("src/Trophy.png"))
stat_img = conv_icone_size(importation("src/Statistics.png"))
lang_img = conv_icone_size(importation("src/Language.png"))
settings_img = conv_icone_size(importation("src/Settings.png"))
play_button = importation("src/fr-buttons/play_button.png") if lang == "fr" else importation("src/en-buttons/play_button.png")

# window setting
win = pygame.display.set_mode((1000, 600))
main_menu(win=win, bg=bg_main_menu_img, tr=tr_img, stat=stat_img, lang_img=lang_img, set=settings_img, button=play_button)

# main loop
_continue = True
while _continue:
    for i in pygame.event.get():
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE] or i.type == pygame.QUIT:
            pygame.quit()
            os.sys.exit(0)
    pygame.display.flip()
