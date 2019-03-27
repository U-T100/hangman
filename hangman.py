# create the hangman
import random

word_list = ["blue","apple","marvel","fire","king"]

def hangman(word):
    wrong = 0
    stages = ["",
              "_______        ",
              "|              ",
              "|      |       ",
              "|      o       ",
              "|     /|\      ",
              "|     / \      ",
              "|              ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("welcome to hangman!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "pridict a character"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages))
        print("you lose!Answer is {}.".format(word))

print(hangman(random.choice(word_list)))
