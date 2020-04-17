# Clément Chapard - QuizzNsi
# This file contains the Soundex algorithm

def soundex(word):
    word.upper()
    word_li = [i for i in word]
    for i in range(len(word_li)) :
        if word_li[i] == " ":
            del word_li[i]
        if i != 0:
            if word_li[i] == "A" or word_li[i] == "E" or word_li[i] == "H" or word_li[i] == "I" or word_li[i] == "O" or word_li[i] == "U" or word_li[i] == "W" or word_li[i] == "Y":
                del word_li

            if word_li[i] == "B" or word_li[i] == "P":
                word_li[i] = "1"
            if word_li[i] == "C" or word_li[i] == "K" or word_li[i] == "Q":
                word_li[i] = "2"
            if word_li[i] == "D" or word_li[i] == "T":
                word_li[i] = "3"
            if word_li[i] == "L":
                word_li[i] = "4"
            if word_li[i] == "M" or word_li[i] == "N":
                word_li[i] = "5"
            if word_li[i] == "R":
                word_li[i] = "6"
            if word_li[i] == "G" or word_li[i] == "J":
                word_li[i] = "7"
            if word_li[i] == "X" or word_li[i] == "Z" or word_li[i] == "S":
                word_li[i] = "8"
            if word_li[i] == "F" or word_li[i] == "V":
                word_li[i] = "9"
        # fin de l'algotithme à ajouter, voir https://fr.wikipedia.org/wiki/Soundex
