
def hangman(word):
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|      |        ",
              "|      O        ",
              "|     /|\       ",
              "|     / \       ",
              "|               "]
              
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

    while wrong < len(stages) -1:
        print("\n")
        msg = "word?"
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
            print("You win!")
            print(" ".join(board))
            win = True
            break
    
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose! The answer is {}.".format(word))

word_list = ["cat", "dog", "water", "tomato", "cup", "glasess", "money"]

import random
r = random.randint(0,len(word_list)-1)
hangman(word_list[r])

            
