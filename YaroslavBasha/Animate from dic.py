# importing modules ploting and animation
import matplotlib.pyplot as p
import matplotlib.animation as a

# animation that takes its input from a dictionary
planets = {
    "0": ["3", "ko", 15],
    "1": ["4", "go", 5],
    "2": ["3", "ro", 6],
    "3": ["2", "yo", 8],
    "4": ["5", "bo", 10],
    "5": ["6", "ro", 20]
}
fig, ax = p.subplots()
max_frames = 6


def animate(frame):
    global ax
    global max_frames
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, 7)
    w = planets.get(str(frame))
    value1 = int(w[0])
    #print(value1)
    attr = w[1]
    attr_clear = "wo"
    value2 = int(w[2])
    #print(value2)
    ax.plot(frame, value1, attr, markersize = value2)


    print("Frame:", frame, "value1", w)


def run():
    global fig
    simple_animation = a.FuncAnimation(fig, animate, frames=max_frames, interval=250)
    p.show()


run()
