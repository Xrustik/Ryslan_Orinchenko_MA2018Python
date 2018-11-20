import simplegui
import random
import math

comp_number = random.randrange(0, 100)
number_life = 7
print("The game starts immediately when the “Run” button")

def start_game(text_input):
    global input
    input = int(text_input)
    print("Your guess was ",input)
    logi_of_game()
    life()
    
def logi_of_game():
    if input < comp_number:
        print("Higher ! ")
        print("Remaning guesses",number_life,'!\n')
    elif input > comp_number:
        print("Lower ! ")
        print("Remaning guesses",number_life,'!\n')
    else:
        print("You win ! \n")
        range100()
        
        

def range100():
    global comp_number
    global number_life
    comp_number = random.randrange(0, 100)
    number_life = 7
    print("Game from 0 to 100 and 7 lives \n ")
    
def range1000():
    global comp_number
    global number_life
    comp_number = random.randrange(0, 1000)
    number_life = 10
    print("Game from 0 to 1000 and 10 lives \n ")
    
def life():
    global number_life
    number_life -= 1
    if number_life == 0 :
        print("GAME OVER ")
        print("secret number =",comp_number,"\n")
        range100()
        

f = simplegui.create_frame("Guess the number",300,300)
f.add_button("range100", range100, 100)
f.add_button("range1000", range1000, 100)
f.add_input("Enter", start_game, 100)

f.start()