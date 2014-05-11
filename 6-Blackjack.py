# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome_ask = ""
outcome_res = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        s = 'Hands contains'
        for card in self.cards: 
            s += ' ' + str(card)
        return s

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        val = 0
        has_aces = False        
        for card in self.cards: 
            val += VALUES[card.get_rank()]
            if has_aces == False and card.get_rank() == 'A':
                has_aces = True
        
        if has_aces:
            val = val + 10 if val + 10 <= 21 else val                
        return val
   
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += CARD_SIZE[0] + 10
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        s = 'Deck contains'
        for card in self.cards:
            s += ' ' + str(card)
        return s


#define event handlers for buttons
def deal():
    global outcome_ask, outcome_res, in_play, deck, dealer_hand, player_hand, score
    
    if in_play: 
        score -= 1

    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
     
    in_play = True
    outcome_ask = 'Hit or stand?'
    outcome_res = ''
    
def hit():
    global in_play, outcome_ask, outcome_res, score
    if in_play == False: return
    
    player_hand.add_card(deck.deal_card())
    print 'Player', player_hand.get_value()
    
    if player_hand.get_value() > 21:
        in_play = False
        outcome_res = 'You went bust and lose.'
        outcome_ask = 'New deal?'
        score -= 1
       
def stand():
    global in_play, outcome_ask, outcome_res, score
    if in_play == False: return

    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())
        print 'Dealer', dealer_hand.get_value()
   
    in_play = False
    outcome_ask = 'New deal?'
    if dealer_hand.get_value() <= 21 and dealer_hand.get_value() >= player_hand.get_value():
        outcome_res = 'You lose.'
        score -= 1
    else:
        outcome_res = 'You win.'        
        score += 1

# draw handler    
def draw(canvas):
    canvas.draw_text('Blackjack', [30, 100], 70, 'Aqua')
    canvas.draw_text('Score ' + str(score), [350, 100], 50, 'Black')
    if in_play:
        canvas.draw_text('Dealer', [30, 180], 30, 'Black')
    else:
        canvas.draw_text('Dealer (' + str(dealer_hand.get_value()) + ')', [30, 180], 30, 'Black')
    
    canvas.draw_text('Player (' + str(player_hand.get_value()) + ')', [30, 350], 30, 'Black')
    canvas.draw_text(outcome_ask, [230, 350], 30, 'Black') 

    pos = (30, 200)
    dealer_hand.draw(canvas, list(pos))     
    player_hand.draw(canvas, [30, 370])      
    
    if in_play:
        pos = [30, 200]
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)    
    else:
        canvas.draw_text(outcome_res, [230, 180], 30, 'Black')    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()