import matplotlib.pyplot as p

x = [0,1,2,3,4,5,6,7]
y = [0,2,3,5,7,7,8,10]

x1 = [1,2,3,4]
y1 = [1,4,3,2]

# subplot 1
p.subplot(2,2,1)
p.plot(x,y,'ro--')
p.xlabel('X1')
p.ylabel('Y1')

# subplot 2
p.subplot(2,2,2)
p.plot(x,y,'yo')

# subplot 3
p.subplot(2,2,3)
p.plot(x,y,'y:')
p.xlabel('X3')
p.ylabel('Y3')

# subplot 4
p.subplot(2,2,4)
p.plot(x1,y1)

# Done!
p.show()