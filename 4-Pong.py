# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]
pad1_pos = pad2_pos = HEIGHT/2
pad1_vel = pad2_vel = 0
score1 = score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    vel_x = random.randrange(120, 240) / 60.0
    vel_y = random.randrange(60, 180) / 60.0 
    vel_x = -vel_x if direction == LEFT else vel_x
    ball_vel = [vel_x, -vel_y]

# define event handlers
def new_game():
    global pad1_pos, pad2_pos, pad1_vel, pad2_vel  # these are numbers
    global score1, score2  # these are ints
    pad1_pos = pad2_pos = HEIGHT/2
    pad1_vel = pad2_vel = 0
    score1 = score2 = 0
    spawn_ball(LEFT)
    
def draw(canvas):
    global score1, score2, pad1_pos, pad2_pos, ball_pos, ball_vel
         
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT-BALL_RADIUS: ball_vel[1] = -ball_vel[1]

    acc = 6
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        if (pad1_pos - HALF_PAD_HEIGHT - acc) <= ball_pos[1] <= (pad1_pos + HALF_PAD_HEIGHT + acc):
            ball_vel[0] = -(ball_vel[0] * 1.1)
        else: 
            score2 += 1
            spawn_ball(RIGHT)
    if ball_pos[0] >= WIDTH-PAD_WIDTH-BALL_RADIUS:
        if (pad2_pos - HALF_PAD_HEIGHT - acc) <= ball_pos[1] <= (pad2_pos + HALF_PAD_HEIGHT + acc):
            ball_vel[0] = -(ball_vel[0] * 1.1)
        else: 
            score1 += 1
            spawn_ball(LEFT)
        
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    pad1_pos += pad1_vel    
    pad2_pos += pad2_vel
    
    if pad1_pos < HALF_PAD_HEIGHT: pad1_pos = HALF_PAD_HEIGHT
    if pad1_pos > HEIGHT - HALF_PAD_HEIGHT: pad1_pos = HEIGHT - HALF_PAD_HEIGHT
        
    if pad2_pos < HALF_PAD_HEIGHT: pad2_pos = HALF_PAD_HEIGHT
    if pad2_pos > HEIGHT - HALF_PAD_HEIGHT: pad2_pos = HEIGHT - HALF_PAD_HEIGHT    
    
    # draw paddles
    canvas.draw_line((HALF_PAD_WIDTH, pad1_pos - HALF_PAD_HEIGHT), (HALF_PAD_WIDTH, pad1_pos + HALF_PAD_HEIGHT), PAD_WIDTH, "White")
    canvas.draw_line((WIDTH - HALF_PAD_WIDTH, pad2_pos - HALF_PAD_HEIGHT), (WIDTH - HALF_PAD_WIDTH, pad2_pos + HALF_PAD_HEIGHT), PAD_WIDTH, "White")
    
    # draw scores
    canvas.draw_text(str(score1), (200, 50), 40, "White")    
    canvas.draw_text(str(score2), (380, 50), 40, "White")    
    
        
def keydown(key):
    global pad1_vel, pad2_vel
    vel = 5;
    if key == simplegui.KEY_MAP['w']: pad1_vel = -vel
    if key == simplegui.KEY_MAP['s']: pad1_vel = vel
    if key == simplegui.KEY_MAP['up']: pad2_vel = -vel
    if key == simplegui.KEY_MAP['down']: pad2_vel = vel
        
   
def keyup(key):
    global pad1_vel, pad2_vel
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']: pad2_vel = 0
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']: pad1_vel = 0    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game)

# start frame
new_game()
frame.start()