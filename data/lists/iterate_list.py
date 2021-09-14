def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions
def menu():
    print("Please select a direction:")
    dirs = directions()
    for index in range(len(dirs)):
        print(f"{index}: {dirs[index]}")
def run():
    menu()

run()
