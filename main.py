# Clément Chapard - QuizzNsi - Python 3.7
# main file of the project

# language definition
file = open('lang.txt', 'r')
lang = str(file.read())
file.close()
_lang = lang

# importation of modules

import pygame
import csv
import os
import random
import time
import statistics as stat
import datetime
import random

if lang == "fr":
    from Soundex_fr import *
elif lang == "en":
    from Soundex_en import *

# window initialization
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = str(1)
win = pygame.display.set_mode((1000, 600))

# images importation
importation = lambda image_name: pygame.image.load(str(image_name)).convert_alpha()
conv_icone_size = lambda image: pygame.transform.scale(image, (50, 50))
conv_param_size = lambda image: pygame.transform.scale(image, (75, 75))

bg_main_menu_img = importation("src/menu_bg.png")
tr_img = conv_icone_size(importation("src/Trophy.png"))
stat_img = conv_icone_size(importation("src/Statistics.png"))
lang_img = conv_icone_size(importation("src/Language.png"))
settings_img = conv_icone_size(importation("src/Settings.png"))
general_bg = importation("src/bg.png")
fr_img = conv_param_size(importation("src/French_flag.png"))
en_img = conv_param_size(importation("src/US_flag.png"))
chrono_img = importation("src/chrono.png")
sound_img = conv_param_size(importation("src/Sound.png"))
no_sound_img = conv_param_size(importation("src/No_sound.png"))
music_img = conv_param_size(importation("src/music.png"))
on_img = conv_param_size(importation("src/ON.png"))
off_img = conv_param_size(importation("src/OFF.png"))
icon = importation("src/icon.png")

if lang == "fr":
    play_button = importation("src/fr-buttons/play_button.png")
    knowledge_button = importation("src/fr-buttons/knowledge_button.png")
    normal_button = importation("src/fr-buttons/normal_button.png")
    speed_button = importation("src/fr-buttons/speed_button.png")
    score_bg = importation("src/fr-buttons/scores_bg.png")
    stat_bg = importation("src/fr-buttons/stats_bg.png")
    play_button_hoover = importation("src/fr-buttons/play_button_hoover.png")
    knowledge_button_hoover = importation("src/fr-buttons/knowledge_button_hoover.png")
    normal_button_hoover = importation("src/fr-buttons/normal_button_hoover.png")
    speed_button_hoover = importation("src/fr-buttons/speed_button_hoover.png")

else:
    play_button = importation("src/en-buttons/play_button.png")
    knowledge_button = importation("src/en-buttons/knowledge_button.png")
    normal_button = importation("src/en-buttons/normal_button.png")
    speed_button = importation("src/en-buttons/speed_button.png")
    score_bg = importation("src/en-buttons/scores_bg.png")
    stat_bg = importation("src/en-buttons/stats_bg.png")
    play_button_hoover = importation("src/en-buttons/play_button_hoover.png")
    knowledge_button_hoover = importation("src/en-buttons/knowledge_button_hoover.png")
    normal_button_hoover = importation("src/en-buttons/normal_button_hoover.png")
    speed_button_hoover = importation("src/en-buttons/speed_button_hoover.png")

# end of images importation

# music and sound importation
file = open('Settings.txt', 'r')
sound_data = str(file.read()).split("/")
file.close()
play_music = True if sound_data[0] == "True" else False
play_sound = True if sound_data[1] == "True" else False
pygame.mixer.init()
music = pygame.mixer.music.load("src/sound/rainy-sun.ogg")
sound = pygame.mixer.Sound("src/sound/clic.ogg")

# csv file importation / creating question list

file = open('quizz_fr.csv' if lang == "fr" else 'quizz_en.csv', encoding='utf-8')
questions_answer_ = [i for i in csv.reader(file, delimiter=";") if
                     i != ['questions', 'reponses'] and i != ['questions', 'answers']]
file.close()
questions_answer = list(questions_answer_)
random.shuffle(questions_answer)

# csv file importation / adding knowledge mode res

file = open('knowledge-res_fr.csv' if lang == "fr" else 'knowledge-res_en.csv', encoding='utf-8')
knowledge_data = [i for i in csv.reader(file, delimiter=";")]
file.close()
for i in range(len(knowledge_data)):
    knowledge_data[i][0] = importation(knowledge_data[i][0])

# window setting

pygame.display.set_caption("E-quizz")
pygame.display.set_icon(icon)

# font setting
text_font = pygame.font.Font("ARLRDBD.TTF", 50)
small_text_font = pygame.font.Font("ARLRDBD.TTF", 25)
medium_text_font = pygame.font.Font("ARLRDBD.TTF", 40)
huge_text_font = pygame.font.Font("ARLRDBD.TTF", 100)


# text formatting

def text_formatting(text, text_ord, text_abs, line_size, choosen_font):
    question_splited = text.split(" ")
    if len(text) < 28:
        win.blit(choosen_font.render(' '.join(question_splited), True, (0, 0, 0)), (190, 100))
    else:
        len_count = 0
        line_li = []
        for k in question_splited:
            len_count += len(k)
            line_li.append(k)
            if len_count > line_size:
                len_count = 0
                txt = choosen_font.render(' '.join(line_li), True, (0, 0, 0))
                win.blit(txt, (text_abs, text_ord))
                line_li = []
                text_ord += 50
        txt = choosen_font.render(' '.join(line_li), True, (0, 0, 0))
        win.blit(txt, (text_abs, text_ord))


# input box

def input_box(text, mode=None, t0=None):
    end_writing = False
    x = 200
    y = 350
    input_box = pygame.Rect(x, y, 600, 70)
    active = True
    while not end_writing:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    end_writing = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    text += ''
                elif len(text) < 12:
                    text += event.unicode
            elif event.type == pygame.QUIT:
                pygame.quit()
                os.sys.exit(0)

        if mode == 5:
            if time.time() - t0 >= 7:
                text = ""
                end_writing = True
            win.blit(chrono_img, (780, 10))
            remaining_time = round(7 - (time.time() - t0), 2)
            txt_time = text_font.render(str(remaining_time), True, (0, 0, 0))
            win.blit(txt_time, (850, 15))

        # Blit the input_box rect.
        pygame.draw.rect(win, (255, 255, 255), input_box)
        # Render the current text.
        txt_surface = text_font.render(text, True, (0, 0, 0))
        # Blit the text.
        win.blit(txt_surface, (x + 5, y + 5))
        pygame.display.flip()
    return text


# animation count

a = 0


# calculating points

tot_pts = []

def points(li, mode, tps=None):
    coef = 1
    tot = 0
    score = 0
    for i in li:
        if i == 1:
            tot += i * coef
            coef += 0.1
            score += 1
        else:
            if coef > 0 :
                coef -= 0.1
    if mode == 5:
        tot *= (tps / (len(questions_answer) * 2.5))
        with open("s_score.txt", "a+") as file:
            file.write("{} pts,{}/{}\n".format(round(tot, 2), score, len(questions_answer)))
        file.close()
    elif mode == 4:
        with open("k_score.txt", "a+") as file:
            file.write("{} pts,{}/{}\n".format(round(tot, 2), score, len(questions_answer)))
        file.close()
    elif mode == 3:
        with open("n_score.txt", "a+") as file:
            file.write("{} pts,{}/{}\n".format(round(tot, 2), score, len(questions_answer)))
        file.close()
    tot = round(tot, 1)
    return tot if tot > 0 else 0


# display the score in the table from a list

def score_display(li, column_abs):
    for i in range(0, 3):
        try:
            s = medium_text_font.render(li[i][:-1], True, (255, 255, 255))
        except IndexError:
            s = text_font.render("          /", True, (255, 255, 255))
        win.blit(s, (column_abs, 210 + i * 125))


# open stats files and create them if they don't exist yet

def import_stat_file(file_):
    try:
        with open(str(file_)) as file:
            return file.readlines()
            file.close()
    except FileNotFoundError:
        with open(str(file_), "w") as file:
            file.close()
        with open("k_score.txt") as file:
            return file.readlines()
            file.close()


# Intro

for i in range(1001):
    if a < 1:
        bg_rect = pygame.Rect(0, 0, 1000, 600)
        pygame.draw.rect(win, (0, 0, 0), bg_rect)
        intro_txt = text_font.render("Clément Chapard", True, (255, 255, 255))
        win.blit(intro_txt, (300, 275))
        pygame.draw.line(win, (255, 255, 255), (500, 0), (1000 * a, 500 * a), 10)
        pygame.draw.line(win, (255, 255, 255), (500, 0), (0 * a, 500 * a), 10)
        pygame.draw.line(win, (255, 255, 255), (500, 600), (0 * a, 100 * a), 10)
        pygame.draw.line(win, (255, 255, 255), (500, 600), (1000 * a, 100 * a), 10)
        a += 0.001
    else:
        time.sleep(2)
    pygame.display.flip()

# main loop

user_view = 1
pygame.mixer.music.play(-1)
while True:
    if not play_music:
        pygame.mixer.music.pause()
    elif play_music:
        pygame.mixer.music.unpause()

    for i in pygame.event.get():
        if (i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE):
            if user_view == 1:
                pygame.quit()
                os.sys.exit(0)

            else:
                if user_view in [2, 6, 7, 8, 9, 10]:
                    user_view = 1
                elif user_view in [3]:
                    user_view = 2
        elif i.type == pygame.QUIT:
            pygame.quit()
            os.sys.exit(0)

        # main menu
        elif user_view == 1:
            background = win.blit(bg_main_menu_img, (0, 0))
            scores_b = win.blit(tr_img, (30, 22))
            stat_b = win.blit(stat_img, (120, 22))
            lang_b = win.blit(lang_img, (210, 22))
            settings_b = win.blit(settings_img, (300, 22))
            play_b = win.blit(play_button, (300, 250))

            if play_b.collidepoint(pygame.mouse.get_pos()):
                play_b = win.blit(play_button_hoover, (300, 250))
                if i.type == pygame.MOUSEBUTTONDOWN:
                    user_view = 2
                    if play_sound: sound.play()
            elif lang_b.collidepoint(
                    pygame.mouse.get_pos()) and i.type == pygame.MOUSEBUTTONDOWN:
                user_view = 6
                if play_sound: sound.play()
            elif scores_b.collidepoint(
                    pygame.mouse.get_pos()) and i.type == pygame.MOUSEBUTTONDOWN:
                user_view = 7
                if play_sound: sound.play()
            elif stat_b.collidepoint(
                    pygame.mouse.get_pos()) and i.type == pygame.MOUSEBUTTONDOWN:
                user_view = 8
                if play_sound: sound.play()
            elif settings_b.collidepoint(
                    pygame.mouse.get_pos()) and i.type == pygame.MOUSEBUTTONDOWN:
                user_view = 9
                if play_sound: sound.play()

        # gamemode choice
        elif user_view == 2:

            background = win.blit(general_bg, (0, 0))
            knowledge_b = win.blit(knowledge_button, (300, 100))
            normal_b = win.blit(normal_button, (300, 250))
            speed_b = win.blit(speed_button, (300, 400))

            if normal_b.collidepoint(pygame.mouse.get_pos()):
                normal_b = win.blit(normal_button_hoover, (300, 250))
                if i.type == pygame.MOUSEBUTTONDOWN:
                    user_view = 3
                    if play_sound: sound.play()
            if knowledge_b.collidepoint(pygame.mouse.get_pos()):
                knowledge_b = win.blit(knowledge_button_hoover, (300, 100))
                if i.type == pygame.MOUSEBUTTONDOWN:
                    user_view = 4
                    if play_sound: sound.play()
            if speed_b.collidepoint(pygame.mouse.get_pos()):
                speed_b = win.blit(speed_button_hoover, (300, 400))
                if i.type == pygame.MOUSEBUTTONDOWN:
                    user_view = 5
                    if play_sound: sound.play()

        # normal mode
        elif user_view == 3:
            with open("time_record", "a+") as file:
                date = datetime.datetime.now()
                file.write(
                    "{},{},{},{},{},{}\n".format(date.year, date.month, date.day, date.hour, date.minute, date.second))
            file.close()
            Ingame_score = 0
            for j in range(len(questions_answer)):
                win.blit(general_bg, (0, 0))
                question = str(questions_answer[j][0])
                text_formatting(question, 100, 190, 17, text_font)
                # fin de la mise en forme du texte
                text = ''
                text = input_box(text)
                if soundex(text) == soundex(str(questions_answer[j][1])):
                    Ingame_score += 1
                    tot_pts.append(1)

                else:
                    tot_pts.append(0)

                #print("réponse : {}, bonne réponse : {}, validé : {} ".format(text, questions_answer[j][1], "oui" if soundex(text) == soundex(str(questions_answer[j][1])) else "non"))

            showScore = True
            pts = points(tot_pts, user_view)
            while showScore:
                for k in pygame.event.get():
                    win.blit(general_bg, (0, 0))
                    txt_score = text_font.render("Score : {}/{}".format(Ingame_score, len(questions_answer_)), True,
                                                 (0, 0, 0))
                    win.blit(txt_score, (100, 100))
                    txt_points = text_font.render("Points : {}".format(pts), True, (0, 0, 0))
                    win.blit(txt_points, (100, 150))
                    pygame.display.flip()
                    if k.type == pygame.KEYDOWN:
                        showScore = False

            random.shuffle(questions_answer)
            user_view = 1

        # Knowledge mode
        elif user_view == 4:
            with open("time_record", "a+") as file:
                date = datetime.datetime.now()
                file.write(
                    "{},{},{},{},{},{}\n".format(date.year, date.month, date.day, date.hour, date.minute, date.second))
            file.close()
            Ingame_score = 0
            for j in range(len(questions_answer_)):
                win.blit(general_bg, (0, 0))
                question = str(questions_answer_[j][0])
                text_formatting(question, 100, 190, 17, text_font)
                # fin de la mise en forme du texte
                text = ''
                text = input_box(text)

                if soundex(text) == soundex(str(questions_answer_[j][1])):
                    Ingame_score += 1
                    tot_pts.append(1)
                else:
                    tot_pts.append(0)

                showKnowledge = True
                while showKnowledge:
                    for k in pygame.event.get():
                        win.blit(general_bg, (0, 0))
                        win.blit(knowledge_data[j][0], (50, 50))
                        text_formatting(knowledge_data[j][1], 50, 400, 30, small_text_font)
                        pygame.display.flip()
                        if k.type == pygame.KEYDOWN:
                            showKnowledge = False
            showScore = True
            pts = points(tot_pts, user_view)
            while showScore:
                for k in pygame.event.get():
                    win.blit(general_bg, (0, 0))
                    txt_score = text_font.render("Score : {}/{}".format(Ingame_score, len(questions_answer_)), True,
                                                 (0, 0, 0))
                    win.blit(txt_score, (100, 100))
                    txt_points = text_font.render("Points : {}".format(pts), True, (0, 0, 0))
                    win.blit(txt_points, (100, 150))
                    pygame.display.flip()
                    if k.type == pygame.KEYDOWN:
                        showScore = False

            # random.shuffle(questions_answer)
            tot_pts = []
            user_view = 1


        # Speed mode
        elif user_view == 5:
            with open("time_record", "a+") as file:
                date = datetime.datetime.now()
                file.write(
                    "{},{},{},{},{},{}\n".format(date.year, date.month, date.day, date.hour, date.minute, date.second))
            file.close()
            tps_tot = time.time()
            Ingame_score = 0
            for j in range(len(questions_answer)):
                tps_q = time.time()
                win.blit(general_bg, (0, 0))
                question = str(questions_answer[j][0])
                text_formatting(question, 100, 190, 17, text_font)
                # fin de la mise en forme du texte
                text = ''
                text = input_box(text, mode=user_view, t0=tps_q)
                if soundex(text) == soundex(str(questions_answer[j][1])):
                    Ingame_score += 1
                    tot_pts.append(1)
                else:
                    tot_pts.append(0)

            tps_tot = round(time.time() - tps_tot, 3)
            showScore = True
            pts = points(tot_pts, mode=user_view, tps=tps_tot)
            while showScore:
                for k in pygame.event.get():
                    win.blit(general_bg, (0, 0))
                    txt_score = text_font.render("Score : {}/{}".format(Ingame_score, len(questions_answer_)), True,
                                                 (0, 0, 0))
                    win.blit(txt_score, (100, 100))
                    txt_points = text_font.render("Points : {}".format(pts),
                                                  True, (0, 0, 0))
                    win.blit(txt_points, (100, 150))
                    pygame.display.flip()
                    if k.type == pygame.KEYDOWN:
                        showScore = False

            random.shuffle(questions_answer)
            user_view = 1


        # Language choice
        elif user_view == 6:
            background = win.blit(general_bg, (0, 0))
            fr_b = win.blit(fr_img, (300, 150))
            fr_text_ = text_font.render("Français" if lang == "fr" else "French", True, (0, 0, 0))
            fr_text = win.blit(fr_text_, (400, 160))
            en_b = win.blit(en_img, (300, 300))
            en_text_ = text_font.render("Anglais" if lang == "fr" else "English", True, (0, 0, 0))
            en_text = win.blit(en_text_, (400, 310))
            text_formatting(
                "/!\ rédémarage nécessaire pour appliquer le changement de langue" if lang == "fr" else "/!\ restart the program to apply modifications",
                400, 50, 17, text_font)

            if (fr_b.collidepoint(pygame.mouse.get_pos()) or fr_text.collidepoint(
                    pygame.mouse.get_pos())) and i.type == pygame.MOUSEBUTTONDOWN:
                lang = "fr"
                file = open('lang.txt', 'w')
                file.write("fr")
                file.close()
                if play_sound: sound.play()
            elif (en_b.collidepoint(pygame.mouse.get_pos()) or en_text.collidepoint(
                    pygame.mouse.get_pos())) and i.type == pygame.MOUSEBUTTONDOWN:
                lang = "en"
                file = open('lang.txt', 'w')
                file.write("en")
                file.close()
                if play_sound: sound.play()

            if lang == "fr":
                highlight = pygame.Rect(290, 140, 330, 100)
                pygame.draw.rect(win, (0, 0, 0), highlight, 5)
            elif lang == "en":
                highlight = pygame.Rect(290, 290, 330, 100)
                pygame.draw.rect(win, (0, 0, 0), highlight, 5)

        # Score
        elif user_view == 7:
            background = win.blit(score_bg, (0, 0))
            k_score_li = import_stat_file("k_score.txt")
            n_score_li = import_stat_file("n_score.txt")
            s_score_li = import_stat_file("s_score.txt")
            for y in [k_score_li, n_score_li, s_score_li]:
                y.sort()
                y.reverse()
            score_display(k_score_li, 65)
            score_display(n_score_li, 365)
            score_display(s_score_li, 665)

        # Stats
        elif user_view == 8:
            background = win.blit(stat_bg, (0, 0))
            k_score_li = import_stat_file("k_score.txt")
            n_score_li = import_stat_file("n_score.txt")
            s_score_li = import_stat_file("s_score.txt")

            for z in [k_score_li, n_score_li, s_score_li]:
                z.sort()
                z.reverse()
            tot_nb_game = medium_text_font.render(str(len(k_score_li) + len(n_score_li) + len(s_score_li)), True,
                                                  (255, 255, 255))
            win.blit(tot_nb_game, (200, 90))
            nb_k_game = medium_text_font.render(str(len(k_score_li)), True, (255, 255, 255))
            win.blit(nb_k_game, (200, 190))
            nb_n_game = medium_text_font.render(str(len(n_score_li)), True, (255, 255, 255))
            win.blit(nb_n_game, (220 if _lang == "fr" else 200, 290))
            nb_s_game = medium_text_font.render(str(len(s_score_li)), True, (255, 255, 255))
            win.blit(nb_s_game, (200, 390))
            if _lang == "fr":
                fav_gamemode = medium_text_font.render(
                    "Culture" if len(k_score_li) > len(n_score_li) and len(k_score_li) > len(s_score_li) else (
                        "Normal" if len(n_score_li) > len(s_score_li) else ("Vitesse" if len(s_score_li) > 0 else "/"))
                    , True, (255, 255, 255))
            elif _lang == "en":
                fav_gamemode = medium_text_font.render(
                    "Knowledge" if len(k_score_li) > len(n_score_li) and len(k_score_li) > len(s_score_li) else (
                        "Normal" if len(n_score_li) > len(s_score_li) else "Speed"), True, (255, 255, 255))
            win.blit(fav_gamemode, (100, 490))
            k_pts_li = [float(i.split(" ")[0]) for i in k_score_li]
            n_pts_li = [float(i.split(" ")[0]) for i in n_score_li]
            s_pts_li = [float(i.split(" ")[0]) for i in s_score_li]
            pts_mean = medium_text_font.render(str(round(stat.mean(k_pts_li + n_pts_li + s_pts_li), 2)) if len(
                k_pts_li + n_pts_li + s_pts_li) > 0 else "/", True, (255, 255, 255))
            win.blit(pts_mean, (440, 90))
            n_pts_mean = medium_text_font.render(str(round(stat.mean(n_pts_li), 2)) if len(n_pts_li) > 0 else "/", True,
                                                 (255, 255, 255))
            win.blit(n_pts_mean, (500, 190))
            k_pts_mean = medium_text_font.render(str(round(stat.mean(k_pts_li), 2)) if len(k_pts_li) > 0 else "/", True,
                                                 (255, 255, 255))
            win.blit(k_pts_mean, (500 if _lang == "fr" else 560, 290))
            s_pts_mean = medium_text_font.render(str(round(stat.mean(s_pts_li), 2)) if len(s_pts_li) > 0 else "/", True,
                                                 (255, 255, 255))
            win.blit(s_pts_mean, (500, 390))
            k_scr_li = [float((i.split(",")[1]).split("/")[0]) for i in k_score_li]
            n_scr_li = [float((i.split(",")[1]).split("/")[0]) for i in n_score_li]
            s_scr_li = [float((i.split(",")[1]).split("/")[0]) for i in s_score_li]
            scr_mean = medium_text_font.render(str(round(stat.mean(k_scr_li + n_scr_li + s_scr_li), 2)) if len(
                k_pts_li + n_pts_li + s_pts_li) > 0 else "/", True, (255, 255, 255))
            win.blit(scr_mean, (740, 90))
            n_scr_mean = medium_text_font.render(str(round(stat.mean(n_scr_li), 2)) if len(n_pts_li) > 0 else "/", True,
                                                 (255, 255, 255))
            win.blit(n_scr_mean, (800, 190))
            k_scr_mean = medium_text_font.render(str(round(stat.mean(k_scr_li), 2)) if len(k_pts_li) > 0 else "/", True,
                                                 (255, 255, 255))
            win.blit(k_scr_mean, (800 if _lang == "fr" else 840, 290))
            s_scr_mean = medium_text_font.render(str(round(stat.mean(s_scr_li), 2)) if len(s_pts_li) > 0 else "/", True,
                                                 (255, 255, 255))
            win.blit(s_scr_mean, (800, 390))
            # dates des parties à completer + debuger quand fichier vide
            game_time = import_stat_file("time_record")
            game_time = [i[:-1].split(",") for i in game_time]
            game_time.sort()
            first_game = small_text_font.render(
                "{}/{}/{} {} {}h{}m{}s".format(game_time[0][2], game_time[0][1], game_time[0][0],
                                               "à" if _lang == "fr" else "at", game_time[0][3], game_time[0][4],
                                               game_time[0][5]) if len(game_time) > 0 else (
                    "Jouez pour compléter" if _lang == "fr" else "Play to complete"), True, (255, 255, 255))
            win.blit(first_game, (370, 500))
            last_game = small_text_font.render(
                "{}/{}/{} {} {}h{}m{}s".format(game_time[-1][2], game_time[-1][1], game_time[-1][0],
                                               "à" if _lang == "fr" else "at", game_time[-1][3], game_time[-1][4],
                                               game_time[-1][5]) if len(game_time) > 0 else (
                    "Jouez pour compléter" if _lang == "fr" else "Play to complete"), True, (255, 255, 255))
            win.blit(last_game, (670, 500))

        # Settings
        elif user_view == 9:
            win.blit(general_bg, (0, 0))

            set_sound_b = win.blit(sound_img if play_sound == True else no_sound_img, (300, 150))
            sound_switch = win.blit(on_img if play_sound == True else off_img, (400, 150))
            if (set_sound_b.collidepoint(pygame.mouse.get_pos()) or sound_switch.collidepoint(
                    pygame.mouse.get_pos())) and i.type == pygame.MOUSEBUTTONDOWN:
                play_sound = False if play_sound == True else True
                if play_sound: sound.play()
                file = open('Settings.txt', 'w')
                file.write("{}/{}".format(play_music, play_sound))
                file.close()
            set_music_b = win.blit(music_img, (300, 300))
            music_switch = win.blit(on_img if play_music == True else off_img, (400, 300))
            if (set_music_b.collidepoint(pygame.mouse.get_pos()) or music_switch.collidepoint(
                    pygame.mouse.get_pos())) and i.type == pygame.MOUSEBUTTONDOWN:
                play_music = (False if play_music == True else True)
                if play_sound: sound.play()
                file = open('Settings.txt', 'w')
                file.write("{}/{}".format(play_music, play_sound))
                file.close()

        # Easter Egg
        if (i.type == pygame.KEYDOWN and i.key == pygame.K_F1):
            user_view = 10
        elif user_view == 10:
            win.blit(general_bg, (0, 0))
            easter_egg_text = huge_text_font.render("Bonjour" if _lang == "fr" else "Hello", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            win.blit(easter_egg_text, (random.randint(0, 1000), random.randint(0, 600)))


    pygame.display.flip()
