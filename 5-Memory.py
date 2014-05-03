# implementation of card game - Memory
import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards, exposed, state, counter
    state = 0
    counter = 0
    label.set_text("Turns = " + str(counter))
    cards = range(0,8) + range(0,8)
    random.shuffle(cards)
    exposed = [False for c in cards]
     
# define event handlers
def mouseclick(pos):
    global state, card1, card2, counter
    index = pos[0] / 50
    if exposed[index]:
        return
    exposed[index] = True
    if state == 0:
        state = 1
        card1 = index
    elif state == 1:
        state = 2
        card2 = index
        counter += 1
        label.set_text("Turns = " + str(counter))
    else:
        if cards[card1] <> cards[card2]:
            exposed[card1] = exposed[card2] = False            
        state = 1    
        card1 = index
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    card_pos = 0
    step = 50
    for i in range(len(cards)):
        if exposed[i]:            
            canvas.draw_text(str(cards[i]), (card_pos+10, 70), 60, 'White')
        else:
            canvas.draw_polygon(((card_pos, 0), (card_pos+step, 0), (card_pos+step, 100), (card_pos, 100)), 2, 'White', 'Green')
        card_pos += step


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()