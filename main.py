# Clément Chapard - QuizzNsi
# main file of the project

# importation of modules

import pygame
import csv
import os
import Soundex
import random
import time

# window initialization
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = str(1)

# images importation
importation = lambda image_name: pygame.image.load(str(image_name))
conv_icone_size = lambda image: pygame.transform.scale(image, (50, 50))

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

# end of images importation

# csv file importation / creating question list

file = open('quizz.csv', encoding='utf-8')
questions_answer = [i for i in csv.reader(file, delimiter=";") if i != ['questions', 'reponses']]
file.close()
random.shuffle(questions_answer)

# window setting
win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("E-quizz")

# font setting
text_font = pygame.font.Font("ARLRDBD.TTF", 50)

# main loop
user_view = 1

_continue = True
while _continue:
    for i in pygame.event.get():
        #key = pygame.key.get_pressed()
        if (i.type == pygame.KEYUP and pygame.K_ESCAPE) or i.type == pygame.QUIT:
            if user_view == 1:
                pygame.quit()
                os.sys.exit(0)
            else:
                user_view = 1
        if user_view == 1:
            background = win.blit(bg_main_menu_img, (0, 0))
            scores_b = win.blit(tr_img, (30, 22))
            stat_b = win.blit(stat_img, (120, 22))
            lang_b = win.blit(lang_img, (210, 22))
            settings_b = win.blit(settings_img, (300, 22))
            play_b = win.blit(play_button, (300, 250))

            if play_b.collidepoint(pygame.mouse.get_pos()) and i.type == pygame.MOUSEBUTTONDOWN:  # ameliorable avec un effet de hoover
                user_view = 2
        elif user_view == 2:

            background = win.blit(general_bg, (0, 0))
            knowledge_b = win.blit(knowledge_button, (300, 100))
            normal_b = win.blit(normal_button, (300, 250))
            speed_b = win.blit(speed_button, (300, 400))

            if normal_b.collidepoint(pygame.mouse.get_pos()) and i.type == pygame.MOUSEBUTTONDOWN:
                user_view = 3

        elif user_view == 3:
            Ingame_score = 0
            for j in range (len(questions_answer)):
                win.blit(general_bg, (0, 0))
                question = str(questions_answer[j][0])
                # mise en forme du texte - améliorable pour gerer plus de ligne
                question_splited = question.split(" ")
                if len(question) > 28:
                    question_part_1 = question_splited[:int(len(question_splited)/2)]
                    question_part_2 = question_splited[int(len(question_splited) / 2):]
                else :
                    question_part_1 = question_splited
                    print(question_part_1)
                    question_part_2 = ""
                question_display_1 = text_font.render(' '.join(question_part_1), True, (0, 0, 0))
                win.blit(question_display_1, (100, 100))
                question_display_2 = text_font.render(' '.join(question_part_2), True, (0, 0, 0))
                win.blit(question_display_2, (100, 150))
                # fin de la mise en forme du texte
                text = ""
                end_writing = False
                x = 200
                y = 300
                input_box = pygame.Rect(x, y, 600, 70)
                active = True
                text = ''
                while not end_writing:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                print(text)
                                end_writing = True
                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                            elif len(text) < 12:
                                text += event.unicode

                    # Blit the input_box rect.
                    pygame.draw.rect(win, (255, 255, 255), input_box)
                    # Render the current text.
                    txt_surface = text_font.render(text, True, (0, 0, 0))
                    # Blit the text.
                    win.blit(txt_surface, (x + 5, y + 5))
                    pygame.display.flip()
                if Soundex.soundex(text) == Soundex.soundex(str(questions_answer[j][1])):
                    Ingame_score += 1
                print(Ingame_score)
            user_view = 1


    pygame.display.flip()
