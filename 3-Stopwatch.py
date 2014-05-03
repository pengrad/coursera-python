# Stopwatch: The Game
import simplegui

# define global variables
time = 0
total = 0
success = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(val):
    m = val / 600
    s = (val % 600) / 10
    ms = val % 10
    str_s = str(s) if s > 9 else "0" + str(s)
    return str(m) + ":" + str_s + "." + str(ms)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    if timer.is_running() == False: return
    global success, total
    timer.stop()
    total += 1
    if time % 10 == 0: 
        success += 1

def reset():
    global time, success, total
    timer.stop()
    time = 0
    success = 0
    total = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), (50, 100), 35, 'White')
    result = str(success) + "/" + str(total)
    canvas.draw_text(result, (130, 30), 20, 'Green')
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 150)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button('Start', start, 100)
frame.add_button('Stop', stop, 100)
frame.add_button('Reset', reset, 100)

# start frame
frame.start()
