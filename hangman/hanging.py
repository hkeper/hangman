import random

def hangman(words):
    word = words[random.randint(0,len(words)-1)]
    print(word)
    wrong = 0
    stages = ["",
              "_____     ",
              "|    |    ",
              "|    0    ",
              "|   /|\   ",
              "|   / \   ",
              "|         "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to execution!")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Enter letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1 
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Win! The word: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Lose! The word: {}.".format(word))

hangman(["cat","dog","tiger"])     

    

