from random import randint

ASCIItable = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def ASCIIconv(number):
    digits = ""
    while number:
        digits += ASCIItable[number%95]
        number //= 95
    return digits

def giveBlock(x,y,z, texture):
    binX = format(x, '08b')
    binY = format(y, '08b')
    binZ = format(z, '08b')
    binTexture = format(texture, '03b')

    bigBin = "1"+binX+binY+binZ+binTexture
    bigInt = int(bigBin, 2)

    return ASCIIconv(bigInt)

def getBlocks(file):
    length = len(file.readline())
    file.seek(0)

    for line in file:
        for i in range(0, length, 5):
            block = line[i:i+5]
            print(block)

world = open('World.txt', 'r+')

for x in range(10):
    for y in range(10):
        for z in range(10):
            block = giveBlock(randint(0,255),randint(0,255),randint(0,255),randint(0,5))
            world.write(block)
        #world.write('\n')
    #world.write('\n\n')






