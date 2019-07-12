# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:49:11 2019

@author: flash
"""

def hangman(word):
    wrong = 0
    stages = ["",
              "_____     ",
              "|    |    ",
              "|    |    ",
              "|    O    ",
              "|   /|\   ",
              "|   / \   ",
              "|         ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")
    
    while wrong < len(stages) - 1:
        print("\n") #ただの空行
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$" #同じ文字が複数含まれる場合への考慮
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
        
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}。".format(word))
        
hangman("earphone")