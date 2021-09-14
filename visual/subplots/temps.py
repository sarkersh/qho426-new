"""
Activity 1: Simple Subplots
We can create subplots using the method subplots of the module pyplot.  This creates the number of subplots specified by
the arguments supplied for the number of rows and columns as shown in the following code fragment:

import matplotlib.pyplot as p

fig, axs = p.subplots(2, 2)
The above creates a 2D list (axs) that we can be used to reference each subplot.  For example, the first subplot is
located at row = 0 and column = 0.  We can target this subplot using the following:

axs[0, 0]

We can also create the subplots such that they share the x axis, the y axis or both:

fig, axs = p.subplots(2, 2, sharex='all')  # all subplots share the x-axis

fig, axs = p.subplots(2, 2, sharex='col')  # only subplots in the same column share the x-axis

fig, axs = p.subplots(2, 2, sharey='row')  # only subplots in the same row share the y-axis
[Tasks]

We wish to create a program to display some data related to temperatures observed during 1 week. The data is as follows:

Day	Temperature
1	18
2	21
3	20
4	21
5	23
6	17
7	16

Data File: You should start by creating a new txt file named temps.txt and store it in the following location:
visual/subplots/temps.txt
This file should contain each temperature value shown in the table above on a new line in your file so that you have 7
lines in your file with each line containing a single temperature value.
"""
import matplotlib.pyplot as p


def read_data(file_path):
    temps = []
    with open(file_path) as file:
        for line in file:
            temps.append(line.strip())
    return temps


def run():
    data = read_data("temps.txt")
    print(data)
    # fig, axs = p.subplots(1, 2)
    # axs[0, 0].plot(range(len(data)), data)
    # axs[0, 1].bar(range(len(data)), data)
    fig, (ax1, ax2) = p.subplots(1, 2)
    ax1.plot(range(len(data)), data)
    ax2.bar(range(len(data)), data)
    p.show()


run()
