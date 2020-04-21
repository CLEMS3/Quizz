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
general_bg = importation("src/bg.png")

if lang == "fr":
    play_button = importation("src/fr-buttons/play_button.png")
    knowledge_button = importation("src/fr-buttons/knowledge_button.png")
    normal_button = importation("src/fr-buttons/normal_button.png")
    speed_button = importation("src/fr-buttons/speed_button.png")

else:
    play_button = importation("src/en-buttons/play_button.png")
    knowledge_button = importation("src/en-buttons/knowledge_button.png")
    normal_button = importation("src/en-buttons/normal_button.png")
    speed_button = importation("src/en-buttons/speed_button.png")

# window setting
win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("E-quizz")

# main loop
user_view = 1
_continue = True
while _continue:
    for i in pygame.event.get():
        print(user_view)
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE] or i.type == pygame.QUIT:
            pygame.quit()
            os.sys.exit(0)
        if user_view == 1:
            main_menu(win=win, bg=bg_main_menu_img, tr=tr_img, stat=stat_img, lang_img=lang_img, set=settings_img,
                      button=play_button, user_view=user_view)
        elif user_view == 2:
            choice_menu(win=win, bg=general_bg, klb=knowledge_button, nmb=normal_button, sdb=speed_button)


    pygame.display.flip()
