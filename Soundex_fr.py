# Clément Chapard - QuizzNsi - Python 3.7
# This file contains the Soundex algorithm

def soundex(word):
    word = word.upper()
    word_li__ = [i for i in word if i not in [" "]]
    word_li = [i for i in word if i not in [" ", "H", "W"]]
    word_li_ = []
    count = 0
    for i in word_li:
        if i != word_li[count - 1] or count == 0:
            word_li_.append(i)
        count += 1

    word_li_2 = []
    for i in range(len(word_li_)):
        if (not word_li_[i] in ["A", "E", "I", "O", "U", "Y"]) or i == 0:
            word_li_2.append(word_li_[i])
    c = 0
    for i in word_li_2:

        if not c == 0:
            if i in ["B", "P"]:
                word_li_2[c] = "1"
            elif i in ["C", "K", "Q"]:
                word_li_2[c] = "2"
            elif i in ["T", "D"]:
                word_li_2[c] = "3"
            elif i in ["L"]:
                word_li_2[c] = "4"
            elif i in ["M", "N"]:
                word_li_2[c] = "5"
            elif i in ["R"]:
                word_li_2[c] = "6"
            elif i in ["G", "J"]:
                word_li_2[c] = "7"
            elif i in ["X", "Z", "S"]:
                word_li_2[c] = "8"
            elif i in ["F", "V"]:
                word_li_2[c] = "9"
        c += 1

    if len(word_li_2) > 4:
        word_li_2 = word_li_2[:4]

    while len(word_li_2) < 4:
        word_li_2.append("0")

    word_li_2[0] = word_li__[0] if len(word_li__) > 0 else 0

    return word_li_2