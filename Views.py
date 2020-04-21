# Clément Chapard - QuizzNsi
# This file contain the directory of differents graphics view of the game

# importation of modules
import pygame

def main_menu(win, bg, tr, stat, lang_img, set, button, user_view):
    background = win.blit(bg, (0, 0))
    scores_b = win.blit(tr, (30, 22))
    stat_b = win.blit(stat, (120, 22))
    lang_b = win.blit(lang_img, (210, 22))
    settings_b = win.blit(set, (300, 22))
    play_b = win.blit(button, (300, 250))

    if play_b.collidepoint(pygame.mouse.get_pos()):
        user_view == 2

    return user_view
#ne marche pas, utiliser enum



def choice_menu(win, bg, nmb, klb, sdb):
    win.blit(bg, (0,0))
    win.blit(nmb, (300, 100))
    win.blit(klb, (300, 250))
    win.blit(sdb, (300, 400))

def game():
    pass

def best_sores():
    pass

def statistics():
    pass

def language_choice():
    pass

def settings():
    pass



