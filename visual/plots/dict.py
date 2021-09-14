import matplotlib.pyplot as p
import random as rnd

def data():
    paths = {}
    print("Please enter the type of line (:, -- or -)?")
    line_style = input()
    print("Please let us know the colour you would like (r, g or b)?")
    colour = input()
    print("please let us know the style of marker you would like (o, S or ^)?")
    marker_style = input()
    paths['line_style'] = line_style
    paths['colour'] = colour
    paths['marker_style'] = marker_style
    return paths

def generate():
    print("How many lines would you like to display?")
    num_lines = int(input())
    for num_line in range(num_lines):
        values = data()
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)
        format = "{}{}{}".format(values['colour'], values['line_style'], values['marker_style'])
        p.plot(x, y, format)
    p.show()


def run():
    print("Running...")
    generate()
    print("Done!")


run()



