import matplotlib.pyplot as p

def coordinate():
    print("Please enter an x value:")
    x = int(input())

    print("Please enter an y value:")
    y = int(input())

    return (x, y)

def path():
    print("Retrieving path...")
    x_values = []
    y_values = []

    for count in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values, y_values]

def run():
    values = path()
    p.plot(values[0], values[1], 'r--o')
    p.xlabel("x values")
    p.ylabel("y values")
    p.show()

run()


