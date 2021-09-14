# Introduction to animations in Python

# Code #1 - proof of concept
import matplotlib.pyplot as p
import matplotlib.animation as a

def spacesheep(fi): # in real life, you will call this animate()
    print('Frame: ', fi)# fi is a variable, frame_index

fig, ax = p.subplots()
simple_animation = a.FuncAnimation(fig, spacesheep, frames = 10, interval = 1000)
p.show()

# Code #2 - little structural change (without affecting functionality)
import matplotlib.pyplot as p
import matplotlib.animation as a

fig, ax = p.subplots()


def spacesheep(fi): # in real life, you will call this animate()
    print('Frame: ', fi)# fi is a variable, frame_index

def run():
    global fig # "sometimes" it works even without this line
    simple_animation = a.FuncAnimation(fig, spacesheep, frames = 10, interval = 1000)
    p.show()

run()

# Code #3 - first real animation
import matplotlib.pyplot as p
import matplotlib.animation as a

fig, ax = p.subplots()
max_frames = 6

def spacesheep(fi): # in real life, you will call this animate()
    global ax, max_frames
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    ax.plot(fi, 5, 'ro')
    if (fi != 0):
        ax.plot(fi-1, 5, 'wo')
    else:
        ax.plot(max_frames-1, 5, 'wo')
    #print('Frame: ', fi)# fi is a variable, frame_index

def run():
    global fig # "sometimes" it works even without this line
    simple_animation = a.FuncAnimation(fig, spacesheep, frames = max_frames, interval = 250)
    # add 'repeat = False' to prevent repeating cycle
    p.show()

run()