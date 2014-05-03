# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random


# initialize global variables used in your code
secret = 0
range = 100
remaining = 7


# helper function to start and restart the game
def new_game():
    global secret, remaining
    secret = random.randrange(0, range)
    remaining = 7 if range == 100 else 10
    print ""
    print "New game. Range is from 0 to", range
    print "Number of remaining guesses is", remaining


# define event handlers for control panel
def range100():
    global range, remaining
    range = 100
    new_game()
    

def range1000():
    global range, remaining
    range = 1000
    new_game()

    
def input_guess(guess):
    global remaining
    remaining = remaining - 1
    iguess = int(guess)
    print ""
    print "Guess was", iguess
    print "Number of remaining guesses is", remaining
    if secret == iguess:
        print "Correct!"
        new_game()
    elif remaining == 0:
        print "You ran out of guesses. The number was", secret
        new_game()
    elif secret > iguess:
        print "Higher!"
    else:
        print "Lower!"

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)	

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game and start frame
new_game()
f.start()