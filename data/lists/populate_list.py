def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    dirs = directions()
    for index in range(len(dirs)):
        print("{}: {}".format(index, dirs[index]))
    index = int(input())
    return dirs[index]
def run():
    route = []
    print("Working out escape route...")
    for count in range(5):
        route.append(menu())
    print(f"Escape route: {route}")
run()


