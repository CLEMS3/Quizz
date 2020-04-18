# Clément Chapard - QuizzNsi
# This file contains the Soundex algorithm

def soundex(word):
    word = word.upper()
    word_li = [i for i in word if i!=" "]
    word_li_2 = []
    for i in range(len(word_li)):
        if ((not word_li[i] in ["A", "E", "H", "I", "O", "U", "W", "Y"]) or i == 0):
            word_li_2.append(word_li[i])
    c = 0
    for i in word_li_2:
        c+=1
        if not c == 1:
            if i in ["B", "P"]:
                word_li_2[word_li_2.index(i)] = "1"
            elif i in ["C", "K", "Q"]:
                word_li_2[word_li_2.index(i)] = "2"
            elif i in ["T", "D"]:
                word_li_2[word_li_2.index(i)] = "3"
            elif i in ["L"]:
                word_li_2[word_li_2.index(i)] = "4"
            elif i in ["M", "N"]:
                word_li_2[word_li_2.index(i)] = "5"
            elif i in ["R"]:
                word_li_2[word_li_2.index(i)] = "6"
            elif i in ["G", "J"]:
                word_li_2[word_li_2.index(i)] = "7"
            elif i in ["X", "Y", "Z"]:
                word_li_2[word_li_2.index(i)] = "8"
            elif i in ["F", "V"]:
                word_li_2[word_li_2.index(i)] = "9"


    return word_li_2


print(soundex("Rupert"))
#[" ", "A", "E", "H", "I", "O", "U", "W", "Y"]