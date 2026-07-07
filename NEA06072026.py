




















asd









world = open("World.txt", "r")

def fileRead(length):
    for line in world:
        for i in range(0, length, 5):
            print(line[i:i+5])


fileRead(25)
