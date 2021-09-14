import matplotlib.pyplot as p

x = [0,1,2,3,4,5,6,7]
y = [0,2,3,5,7,7,8,10]

x1 = [1,2,3,4]
y1 = [1,4,3,2]


x2 = [1,2,3,100]
y2 = [1,4,3,2]

fig, axs = p.subplots(2,2, sharex='col')
axs[0,0].plot(x2,y2,'ro--')
axs[0,1].plot(x,y,'yo')
axs[1,0].plot(x,y,'y:')
axs[1,1].plot(x1,y1)


# Done!
p.show()