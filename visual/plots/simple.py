import matplotlib.pyplot as p
"""
x = [0, 2, 4, 6, 8, 10]
y = [0, 20, 40, 60, 80, 100]

p.xlabel("x values")
p.ylabel("y values")
***plot, step and bar***
p.plot(x, y, "ro")         # The function is used to create line graphs or display markers.
p.step(x, y)               # This function is similar to the plot function but is used to create a step plot.
p.bar(x, y)                # This function is used to create a histogram.
p.show()
***pie chart***
labels = ('A','B', 'C', 'D', 'E')
sizes = [15, 30,45, 10, 25]

p.pie(sizes, labels = labels) # This function is used to create a pie chart.
p.show()
"""
# Activity 1: Simple Line Plot
def display(x,y):
    p.xlabel("x values")
    p.ylabel("y values")
    p.plot(x, y)
    p.show()

def run():
    print("Running...")
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    display(x_values, y_values)

run()













