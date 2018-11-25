import simplegui

sec = 0
minute = 0
message = "0:00.0"

accounts = "0/0"
victory = 0
defeat = 0

def start():
    global message
    global sec
    global minute
    timer.start()
    sec += 0.1
    if sec >59.9:
        minute += 1
        sec = 0
    if sec > 10:
        message = str(minute)+":"+str(sec)
    else:
        message = str(minute)+":0"+str(sec)
        
def stop():
    timer.stop()
    convert(sec)
    
def convert(val):
    global victory
    global defeat
    global accounts
    accounts = int(val)
    msec = int(round(10 * (val - accounts)))
    
    if msec == 0:
        victory += 1
    else:
        defeat += 1
    accounts = str(victory)+"/"+str(defeat)
    
def remov():
    global message
    global sec
    global minute
    sec = 0
    minute = 0
    message = "0:00.0"
    

def draw(canvas):
    canvas.draw_text(message, [50,120], 48, "Red")
    canvas.draw_text(accounts, [160,20], 20, "Red")

frame = simplegui.create_frame("Home", 200, 200)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Remov", remov)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, start)

frame.start()
