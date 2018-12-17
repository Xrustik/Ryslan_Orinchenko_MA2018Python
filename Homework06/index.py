import simplegui
import random

CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

in_play = False
outcome = ""
score = 0
win = 0
loss = 0

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0

    def __str__(self):
        temp="hand contains "
        for car in self.cards:
            temp+=str(car)+" "
        return temp   

    def add_card(self, card):
        self.cards.append(card)
        self.value+=VALUES[card.rank]

    def get_value(self):
        a=[car for car in self.cards if car.get_rank()!='A']
        self.value=0
        for car in a:
           self.value+=VALUES[car.get_rank()]
        if len(a)==len(self.cards):
            return self.value
        else:
            if self.value<12:
                if self.value==10 and (len(self.cards)-len(a))==2:
                    return 12
                for i in range(len(self.cards)-len(a)):
                    if self.value+11<=21:
                        self.value+=11
                    else:
                        self.value+=1
                return self.value
            else:
                for i in range(len(self.cards)-len(a)):
                    self.value+=1
                return self.value            
   
    def draw(self, canvas, pos):
        i=0
        for car in self.cards:
            car.draw(canvas,[pos[0]+i*100,pos[1]])
            i+=1
            
class Deck:
    def __init__(self):
        self.cards=[]

        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit,rank))
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        temp="Deck contains "
        for car in self.cards:
            temp+=str(car)+" "
        return temp

    
def deal(): 
    global outcome, in_play, deck, score, win, loss
    
    if(in_play==True):
        outcome= "Foul play. Dealer wins"
        in_play=False
        loss+=1
    elif(in_play==False):
        
        deck=Deck()
        dealer.cards=[]
        player.cards=[]
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        in_play = True

def hit():
    global outcome, in_play, score, loss, win

    if(in_play==True):
        player.add_card(deck.deal_card())
        
        if(player.get_value()>21 and in_play==True):
            outcome="You have busted. Dealer wins"
            in_play=False
            loss+=1
    
def stand():
    global outcome, in_play, score, win, loss
    
    if(in_play==True and dealer.get_value()<18):
        while(dealer.get_value()<18):
            dealer.add_card(deck.deal_card())
        stand()
    elif(in_play==True and dealer.get_value()>21):
        outcome="Dealer busted, YOU WIN!"
        in_play=False
        win+=1
    elif(in_play==True and player.get_value()<=dealer.get_value()):
        outcome="Dealer wins!"
        in_play=False
        loss+=1
    elif (in_play==True):
        outcome="YOU WIN!"
        in_play=False
        win+=1
         
def draw(canvas):
    global win, loss
   
    player.draw(canvas,[50,400])
    dealer.draw(canvas,[50,200])
    if(in_play):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,[50+36.5,200+49] , CARD_BACK_SIZE)
    
    canvas.draw_text("Blackjack", [50, 50], 36, "RED")
    canvas.draw_text("Dealer", [50, 100], 28, "Black")
    canvas.draw_text("Wins: "+str(win), [250, 50], 28, "Black")
    canvas.draw_text("Losses: "+str(loss), [450, 50], 28, "Black")
    
    if(not in_play):
        canvas.draw_text("New Deal?", [150, 350], 28, "Black")
        canvas.draw_text(outcome, [150, 100], 28, "Black")
        
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

frame.add_button("Deal", deal, 150)
frame.add_button("Hit",  hit, 150)
frame.add_button("Stand", stand, 150)
frame.set_draw_handler(draw)

frame.start()
player = Hand()
dealer = Hand()
deck = Deck()
deal()