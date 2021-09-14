import matplotlib.pyplot as p

def small():
    x = [3, 3,4, 4, 3]
    y = [3, 4, 4, 3, 3]
    p.plot(x, y, 'r:o')

def medium():
    x = [2, 2, 5, 5, 2]
    y = [2, 5, 5, 2, 2]
    p.plot(x, y, 'g--s')

def large():
    x = [1, 1, 6, 6, 1]
    y = [1, 6, 6, 1, 1]
    p.plot(x, y, 'b-s')

def run():
    small()
    medium()
    large()
    p.show()

run()
