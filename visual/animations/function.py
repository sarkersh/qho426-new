"""
Activity 1: Basic Function
We can create animations using matplotlib by importing the module animation:

import matplotlib.pyplot as plt
import matplotlib.animation as animation

The module contains the function FuncAnimation which allows us to create an animation. This function works by repeatedly
calling a user-defined function to draw a frame of the animation. The function FuncAnimation takes a number of parameters
including:
- fig: This is the figure to which the animation is drawn
- func: This is the user-defined function which we wish to call in order to draw a frame of our animation
- frames: These are the frames that make up our animation.
- interval: This is the delay between frames in milliseconds
An example usage of the function is as follows:

def animate(frame):
    pass
fig, ax = plt.subplots()
some_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 100)

In the above example, we create a user-defined function named animate which takes a single parameter named frame. This
function is responsible for drawing a single frame of our animation.  We then use FuncAnimation to repeatedly call our
function every 100 milliseconds for 10 frames.  By default, the animation is set to repeat but we can stop this by
providing a False value for the parameter repeat:

some_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 100, repeat = False)
"""
import matplotlib.pyplot as p
import matplotlib.animation as a

def animate(frame):
    print(f"Frame:", {frame})

def run():
    fig, ax = p.subplots()
    simple_animation = a.FuncAnimation(fig, animate, frames=10, interval=1000)
    p.show()

run()