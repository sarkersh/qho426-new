# Introduction to animations in Python
import matplotlib.pyplot as p
import matplotlib.animation as a


def animate(frame):
    print("Frame:", frame)


fig, ax = p.subplots()
simple_animation = a.FuncAnimation(fig, animate, frames=10, interval=1000)
p.show()
#Little structural change (without affecting functionality)
#import matplotlib.pyplot as p
#import matplotlib.animation as a

fig, ax = p.subplots()


def animate(frame):
    print("Frame:", frame)


def run():
    global fig
    simple_animation = a.FuncAnimation(fig, animate, frames=10, interval=1000)
    p.show()


run()

# First real animation
import matplotlib.pyplot as p
import matplotlib.animation as a

fig, ax = p.subplots()
max_frames = 10


def animate(frame):
    global ax
    global max_frames
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.plot(frame, 5, "ro")
    if (frame != 0):
        ax.plot(frame - 1, 5, "wo")
    else:
        ax.plot(max_frames - 1, 5, "wo")
    print("Frame:", frame)
    # return line


def run():
    global fig
    simple_animation = a.FuncAnimation(fig, animate, frames=max_frames, interval=250)
    p.show()


run()
