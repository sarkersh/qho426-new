# import graphical library
import matplotlib.pyplot as p

# define data - Num + Num
x = [0, 1, 3, 5, 7, 7, 8]
y = [0, 2, 3, 5, 7, 8, 9]

# set diagram parameters
p.xlabel('X - Independent')
p.ylabel('Y - Independent')

# plot!
p.plot(x, y, 'o')
p.plot(x, y, '')
p.plot(x, y, 'yo')
