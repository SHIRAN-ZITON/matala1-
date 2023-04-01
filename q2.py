# -*- coding: utf-8 -*-
"""
@author: shiran.ziton
"""

def revword(word:str):
            word = word.lower()[::-1]
            return word


def countword():
    text = open("text.txt","r")
    count = 1
    for i in text:
        list_words = i.split()
        if len(list_words)==1:
            first_w = list_words[0].lower().strip()
        else:
            for j in list_words :
                w = revword(j).strip()
                if w == first_w:
                    count += 1
    print(count)

countword()

