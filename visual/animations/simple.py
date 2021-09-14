import matplotlib.pyplot as p
import matplotlib.animation as a

# fig, ax = p.subplots()
#
# def animate(frame):
#     global ax
#     # your code here (use ax to draw)
#     ax.set_xlim(0, 10)
#     ax.set_ylim(0, 10)
#     ax.plot(range(frame), range(frame))
#
#
#
# def run():
#     global fig
#     # your code here (use fig with animation function)
#     simple_animation = a.FuncAnimation(fig, animate, frames = 10, interval = 1000)
#     p.show()
#
#
# run()
# Alternative solution using a 2D line:


line = None

def animate(frame):
    global line
    line.set_data(range(frame), range(frame))


def run():
    global line
    fig, ax = p.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    line, = ax.plot([], [], 'ro')
    simple_animation = a.FuncAnimation( fig,
                                        animate,
                                        frames = 10,
                                        interval = 1000)

    p.show()

run()













