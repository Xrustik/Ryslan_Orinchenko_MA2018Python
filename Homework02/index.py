import simplegui
import random
import math

comp_number = random.randrange(0, 100)
l = 7


def enter(text_input):
    global input
    input = int(text_input)
    print("Your guess was ", input)
    logik()
    life()


def logik():
    if (input < comp_number):
        print("Higher ! ")
        print("Remaning guesses !", l, '\n')
    elif (input > comp_number):
        print("Lower ! ")
        print("Remaning guesses !", l, '\n')
    else:
        print("You win ! \n")
        range100()


def range100():
    global comp_number
    global l
    comp_number = random.randrange(0, 100)
    l = 7
    print("Game from 0 to 100 and 7 lives \n ")


def range1000():
    global comp_number
    global l
    comp_number = random.randrange(0, 1000)
    l = 10
    print("Game from 0 to 1000 and 10 lives \n ")


def life():
    global l
    l -= 1
    if (l == 0):
        print("GAME OVER ")
        print("secret number =", comp_number, "\n")
        range100()


# create frame
f = simplegui.create_frame("Guess the number", 300, 300)

# register event handlers
f.add_button("range100", range100, 100)
f.add_button("range1000", range1000, 100)
f.add_input("Enter", enter, 100)

# get frame rolling
f.start()