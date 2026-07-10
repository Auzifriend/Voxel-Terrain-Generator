#==============================================================================#
#=  Data Layer                                                                =#
#==============================================================================#

#file-initialisation------------------------------------------------------------

def initialiseWorld(length, width, height, file):

    if not(0 < length <= 64) or not(0 < width <= 64) or not(0 < height <= 32):  #user world size parameters  validation
        return -1                                                               #returns -1 if not valid -> main file will  do something with this

    line = "N" * length * width * height                                        #calculates how many blocks in world,  uses "N" as 'no texture'
    file.write(line)                                                            #writes all blocks to the world file

#changing-block-texture-in-file-------------------------------------------------

def changeBlock(x,y,z, texture, file):
    index = x + 5*y + 25*z                                                      #calculates index in world file based on  xyz input
    file.seek(index)                                                            #sets file pointer to the index
    file.write(texture)                                                         #writes the new texture character to the index -> different textures represented with different characters

#main---------------------------------------------------------------------------

##for tests, will  be different after presentation and logic layers made

with open("World.txt", "w") as world:
    initialiseWorld(5,5,5,world)
    changeBlock(2,2,1,"6",world)
