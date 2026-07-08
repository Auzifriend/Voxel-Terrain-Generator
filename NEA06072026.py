#===============================================================================
#= Data Layer (handles block data conversion to and from the text file)       =#
#===============================================================================

#ASCII-conversions--------------------------------------------------------------

ASCIItable = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def numToASCII(number):
    digits = ""
    while number:
        digits += ASCIItable[number%95]
        number //= 95
    return digits[::-1]

def ASCIItoNum(digits):
    number = 0
    for i in range(4):
        Index = ASCIItable.index(digits[i])
        number = number * 95 + Index
    return number

#text-file-interactions---------------------------------------------------------

def giveBlock(x,y,z, texture):
    binX = format(x, '08b')
    binY = format(y, '06b')
    binZ = format(z, '08b')
    binTexture = format(texture, '03b')

    bigBin = "1"+binX+binY+binZ+binTexture
    bigInt = int(bigBin, 2)

    return numToASCII(bigInt)

def getBlocks(file):
    length = len(file.readline())
    file.seek(0)

    for i in range(0, length, 5):
        block = file.read(5)

        bigInt = ASCIItoNum(block)
        bigBin = format(bigInt, '026b')

        decX = int(bigBin[1:9], 2)
        decY = int(bigBin[9:15], 2)
        decZ = int(bigBin[15:23], 2)
        decTexture = int(bigBin[23:], 2)

        print(decX, decY, decZ, decTexture)

#main---------------------------------------------------------------------------

with open("World.txt", "r+") as world:
    #world.write(giveBlock(67,63,42,5))
    getBlocks(world)
