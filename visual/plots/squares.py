"""
Activity 2: Squares with Line Plot
We can control various aspects of the plot including the shape, size and colour:
* marker styles can be specified using single characters
* these include o for circles, s for squares, ^ for triangle up, v for triangle down
p.plot(x, y, 'o')       # 'o' will display circle makers
p.plot(x, y, 's')       # 's' will display square makers
* similarly, we can control the line styles :-
 these include - for solid lines, -- for dashed lines, -. for dash-dot lines, : for dotted lines
p.plot(x, y, 'o-')      # will display circle markers with a solid line
p.plot(x, y, 'o--')     # will display circle markers with a dashed line
p.plot(x, y, 'o:')      # will display circle markers with a dotted line
* colors can be specified using single characters where r is red, b is blue, g is green, etc.
* supported colours include red, blue, green, cyan, magenta, yellow, black and white.
p.plot(x, y, 'yo')   # will display yellow markers
p.plot(x, y, 'ro--') # will display a red dashed line
"""
import matplotlib.pyplot as p


def small():
    x = [3, 3, 4, 4, 3]
    y = [3, 4, 4, 3, 3]
    p.plot(x, y, 'ro:')


def medium():
    x = [2, 2, 5, 5, 2]
    y = [2, 5, 5, 2, 2]
    p.plot(x, y, 'g--s')


def large():
    x = [1, 1, 6, 6, 1]
    y = [1, 6, 6, 1, 1]
    p.plot(x, y, 'b-p')


def run():
    small()
    medium()
    large()
    p.show()

run()
