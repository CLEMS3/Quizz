# Clément Chapard - QuizzNsi
# This file contains the Soundex algorithm

def soundex(word):
    word = word.upper()
    word_li = [i for i in word]
    word_li_origin = list(word_li)
    i = 0
    while i <= len(word_li):
        print(i)
        if word_li_origin[i] == word_li_origin[i - 1]:
            del word_li[i]
            i-=1
        print(word_li)
        try:
            if word_li_origin[i] == word_li_origin[i + 1]:
                del word_li[i + 1]
                i -= 1
        except IndexError:
            pass
        print(word_li)
        if i != 0:
            if word_li[i] == "A" or word_li[i] == "E" or word_li[i] == "H" or word_li[i] == "I" or word_li[i] == "O" or word_li[i] == "U" or word_li[i] == "W" or word_li[i] == "Y" or word_li[i] == " ":
                del word_li[i]
                i -= 1
            elif word_li[i] == "B" or word_li[i] == "P":
                word_li[i] = "1"
            elif word_li[i] == "C" or word_li[i] == "K" or word_li[i] == "Q":
                word_li[i] = "2"
            elif word_li[i] == "D" or word_li[i] == "T":
                word_li[i] = "3"
            elif word_li[i] == "L":
                word_li[i] = "4"
            elif word_li[i] == "M" or word_li[i] == "N":
                word_li[i] = "5"
            elif word_li[i] == "R":
                word_li[i] = "6"
            elif word_li[i] == "G" or word_li[i] == "J":
                word_li[i] = "7"
            elif word_li[i] == "X" or word_li[i] == "Z" or word_li[i] == "S":
                word_li[i] = "8"
            elif word_li[i] == "F" or word_li[i] == "V":
                word_li[i] = "9"
            print(word_li)
        i += 1

    soundex_code = []
    for i in range(0, 4):
        try:
            soundex_code.append(word_li[i])
        except IndexError:
            pass
        if len(soundex_code)<4:
            soundex_code.append("0")

    return soundex_code


print(soundex(" b"))
