import random

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return -1


def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'error'

    

def rpsls(player_choice): 
    print ''
    print 'Player chooses', player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_name = number_to_name(comp_number)
    print 'Computer chooses', comp_name
    diff = player_number - comp_number
    if diff == 0:
        print 'Player and computer tie!'
    elif diff > 0:
        print 'Player wins!' if diff < 3 else 'Computer wins!'
    else:
        print 'Player wins!' if (5 + diff) < 3 else 'Computer wins!'        
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")