# Clément Chapard - QuizzNsi
# main file of the project

# language definition
file = open('lang.txt', 'r')
lang = str(file.read())
file.close()

# importation of modules

import pygame
import csv
import os
import random
import time
if lang == "fr":
    from Soundex_fr import *
elif lang == "en":
    from Soundex_en import *
# window initialization
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = str(1)

# images importation
importation = lambda image_name: pygame.image.load(str(image_name))
conv_icone_size = lambda image: pygame.transform.scale(image, (50, 50))

bg_main_menu_img = importation("src/menu_bg.png")
tr_img = conv_icone_size(importation("src/Trophy.png"))
stat_img = conv_icone_size(importation("src/Statistics.png"))
lang_img = conv_icone_size(importation("src/Language.png"))
settings_img = conv_icone_size(importation("src/Settings.png"))
general_bg = importation("src/bg.png")
fr_img = pygame.transform.scale(importation("src/French_flag.png"), (75, 75))
en_img = pygame.transform.scale(importation("src/US_flag.png"), (75, 75))

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

file = open('quizz_fr.csv' if lang == "fr" else 'quizz_en.csv', encoding='utf-8')
questions_answer_ = [i for i in csv.reader(file, delimiter=";") if i != ['questions', 'reponses'] and i != ['questions', 'answers']]
file.close()
questions_answer = list(questions_answer_)
random.shuffle(questions_answer)

# csv file importation / adding knowledge mode res

file = open('knowledge-res_fr.csv' if lang == "fr" else 'knowledge-res_en.csv', encoding='utf-8')
knowledge_data = [i for i in csv.reader(file, delimiter=";")]
file.close()



# window setting
win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("E-quizz")

# font setting
text_font = pygame.font.Font("ARLRDBD.TTF", 50)


# text formatting

def text_formatting(text, text_ord, text_abs):
    question_splited = text.split(" ")
    if len(text) < 28:
        win.blit(text_font.render(' '.join(question_splited), True, (0, 0, 0)), (190, 100))
    else:
        len_count = 0
        line_li = []
        for k in question_splited:
            len_count += len(k)
            line_li.append(k)
            if len_count > 17:
                len_count = 0
                txt = text_font.render(' '.join(line_li), True, (0, 0, 0))
                win.blit(txt, (text_abs, text_ord))
                line_li = []
                text_ord += 50
        txt = text_font.render(' '.join(line_li), True, (0, 0, 0))
        win.blit(txt, (text_abs, text_ord))

# input box

def input_box(text):
    end_writing = False
    x = 200
    y = 350
    input_box = pygame.Rect(x, y, 600, 70)
    active = True
    while not end_writing:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(text)
                    end_writing = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    text += ''
                elif len(text) < 12:
                    text += event.unicode

        # Blit the input_box rect.
        pygame.draw.rect(win, (255, 255, 255), input_box)
        # Render the current text.
        txt_surface = text_font.render(text, True, (0, 0, 0))
        # Blit the text.
        win.blit(txt_surface, (x + 5, y + 5))
        pygame.display.flip()
    return text


# main loop
user_view = 1

_continue = True
while _continue:
    for i in pygame.event.get():
        if (i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE ):
            if user_view == 1:
                print("exit")
                pygame.quit()
                os.sys.exit(0)

            else:
                if user_view in [2, 6]:
                    user_view = 1
                elif user_view in [3]:
                    user_view = 2
        elif i.type == pygame.QUIT:
            print("exit")
            pygame.quit()
            os.sys.exit(0)

        # main menu
        if user_view == 1:
            background = win.blit(bg_main_menu_img, (0, 0))
            scores_b = win.blit(tr_img, (30, 22))
            stat_b = win.blit(stat_img, (120, 22))
            lang_b = win.blit(lang_img, (210, 22))
            settings_b = win.blit(settings_img, (300, 22))
            play_b = win.blit(play_button, (300, 250))

            if play_b.collidepoint(
                    pygame.mouse.get_pos()) and i.type == pygame.MOUSEBUTTONDOWN:  # ameliorable avec un effet de hoover
                user_view = 2
            elif lang_b.collidepoint(
                    pygame.mouse.get_pos()) and i.type == pygame.MOUSEBUTTONDOWN:  # ameliorable avec un effet de hoover
                user_view = 6

        # gamemode choice
        elif user_view == 2:

            background = win.blit(general_bg, (0, 0))
            knowledge_b = win.blit(knowledge_button, (300, 100))
            normal_b = win.blit(normal_button, (300, 250))
            speed_b = win.blit(speed_button, (300, 400))

            if normal_b.collidepoint(pygame.mouse.get_pos()) and i.type == pygame.MOUSEBUTTONDOWN:
                user_view = 3
            elif knowledge_b.collidepoint(pygame.mouse.get_pos()) and i.type == pygame.MOUSEBUTTONDOWN:
                user_view = 4

        # normal mode
        elif user_view == 3:
            Ingame_score = 0
            for j in range(len(questions_answer)):
                win.blit(general_bg, (0, 0))
                question = str(questions_answer[j][0])
                text_formatting(question, 100, 190)
                # fin de la mise en forme du texte
                text = ''
                text = input_box(text)
                if soundex(text) == soundex(str(questions_answer[j][1])):
                    Ingame_score += 1
                print("score : ",Ingame_score)
            random.shuffle(questions_answer)
            user_view = 1
        elif user_view == 4:
            Ingame_score = 0
            for j in range(len(questions_answer_)):
                win.blit(general_bg, (0, 0))
                question = str(questions_answer_[j][0])
                text_formatting(question, 100, 190)
                # fin de la mise en forme du texte
                text = ''
                text = input_box(text)
                if soundex(text) == soundex(str(questions_answer_[j][1])):
                    Ingame_score += 1
                win.blit(general_bg, (0,0))
                win.blit(importation(knowledge_data[questions_answer_.index(questions_answer[j])-1][0]), (0,0))
                print("score : ", Ingame_score)
            random.shuffle(questions_answer)
            user_view = 1

        # language choice
        elif user_view == 6:
            background = win.blit(general_bg, (0,0))
            fr_b = win.blit(fr_img, (300, 150))
            fr_text_ = text_font.render("Français" if lang == "fr" else "French", True, (0, 0, 0))
            fr_text = win.blit(fr_text_, (400, 160))
            en_b = win.blit(en_img, (300, 300))
            en_text_ = text_font.render("Anglais" if lang == "fr" else "English", True, (0, 0, 0))
            en_text = win.blit(en_text_, (400, 310))
            text_formatting("/!\ rédémarage nécessaire pour appliquer le changement de langue" if lang == "fr" else "/!\ restart the program to apply modifications", 400, 50)

            if fr_b.collidepoint(pygame.mouse.get_pos()) and i.type == pygame.MOUSEBUTTONDOWN:
                lang = "fr"
                file = open('lang.txt', 'w')
                file.write("fr")
                file.close()
            elif en_b.collidepoint(pygame.mouse.get_pos()) and i.type == pygame.MOUSEBUTTONDOWN:
                lang = "en"
                file = open('lang.txt', 'w')
                file.write("en")
                file.close()

            if lang == "fr":
                highlight = pygame.Rect(290, 140, 330, 100)
                pygame.draw.rect(win, (0, 0, 0), highlight, 5)
            elif lang == "en":
                highlight = pygame.Rect(290, 290, 330, 100)
                pygame.draw.rect(win, (0, 0, 0), highlight, 5)


    pygame.display.flip()
