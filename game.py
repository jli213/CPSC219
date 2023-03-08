"""
Jessica LI UCID: 30180801
Tutorial Section: T14
Program Version: 1
Version Date: 12-03
features: a text-based biological simulation: Conway's "Game of Life". 
        Given a starting pattern of life forms that comes either from: 
        1) one of the 6 hard-coded (fixed) starting patterns in the starting code OR 
        2) read in from file 
        program will apply the [rules of births and deaths] on a turn-by-turn basis. 
        At the end of each turn the before and after state of the simulation will be displayed to the user. 
        There will then be an option to continue the simulation or quit the program/ If the 'hidden' option is selected then [debugging mode] will be toggled.
"""


SIZE = 10

#constants for characters in input file
EMPTY = ""
TAB = "\t"
SPACE = " "
NEWLINE = "\n"

#global variable:debug flag
debugOn = False



#Game of Life simulation
#Author:  James Tam
#Version: June 6, 2020
#This version of the program initializes the oldWorld (during the turn)
#and the newWorld (appearance of the world after the turn) as well as
#displaying the two versions side by side. Since the original state of
#the biosphere was empty the state of the new state is correct. However,
#no rules of births and deaths was applied in this version of the
#simulation.

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @oneEmpty()
  @Arguments: None
  @The biosphere is initialized to a completely empty state.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def oneEmpty():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @twoSingleCritter()
  @Arguments: None
  @The biosphere is empty except for one location which contains a 
  @Critter.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def twoSingleCritter():
    world = []
    world = [
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @threeSingleBirth()
  @Arguments: None
  @The biosphere is empty except for 3 locations which contain Critters.
  @The 3 Critters are all in proximity to a single location in the 
  @biosphere.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def threeSingleBirth():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " ","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @fourthSimpleBirth()
  @Arguments: None
  @The biosphere contains a number of Critters which are close enough
  @proximity to produce new births for a number of turns.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def fourthSimpleBirth():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", "*","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " ","*", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @fifthCreateListEdgeCases()
  @Arguments: None
  @The biosphere has a Critter located at the edge of the biosphere at
  @each of the 4 compass ponts. Also there is a Critter in each of the
  @corners.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def fifthCreateListEdgeCases():
    world = []
    world = [
     ["*"," ", "*"," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", "*", " "],
     ["*","*", " "," ", " ", " ", " ", " ", " ", "*"]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @sixthComplexCases()
  @Arguments: None
  @The biosphere contains a starting pattern that will require a 
  @program to handle births, deaths and edge cases. 
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def sixthComplexCases():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", "*", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", "*", " ", " ", " ", " "],
     [" "," ", " ","*", "*", "*", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
# '''
# @display()
# @Argument: two references to the 2D list which is game world.
# @The list must be already created and properly initialized
# @prior to calling this function!
# @Return value: None
# @Displays each element of the world with each row all on one line
# @Each element is bound: above, left, right and below with a bar (to
# @make elements easier to see.
# @Each list is displayed side by side
# <Old list>#<TAB><New list>
# '''
def display(turn,oldWorld,newWorld):
    numRows = len(oldWorld)
    numCols = len(oldWorld[0])
    # Displays a row at a time of each list
    print("Turn #%d" %turn)
    print("BEFORE\t\t\t\tAFTER")
    for r in range (0,numRows,1):

        # Row of dashes before each row of old and new list
        # (Dashes for old list)
        for i in range (0, numCols, 1): 
            print("%s" %(" -"), end="")
        print("#\t",end="")
        # (Dashes for new list)
        for i in range (0, numCols, 1): 
            print("%s" %(" -"), end="")
        print()

        # Display one row of old world list
        for c in range (0,numCols,1):
            # Display: A vertical bar and then element (old list) 
            print("|%s" %(oldWorld[r][c]), end = "")
        # Separate the lists with a number sign and a tab
        print("", end = "#\t")    

        # Display one row of new world list
        for c in range (0,numCols,1):
            # Display: A vertical bar and then element (new list) 
            print("|%s" %(newWorld[r][c]), end = "")
        print("|")

    # Row of dashes after end of last row (old world list)
    for i in range (0, numCols, 1): 
        print("%s" %(" -"), end="")
    print("#\t",end="")

    # Row of dashes after end of each row (new world list)
    for i in range (0, numCols, 1): 
        print("%s" %(" -"), end="")
    print()

#fileRead()
#function will 
#Prompt the user for the name of the input file & if the file is empty it will display an error message.
#Open the input file and read the starting information from any arbitrarily sized rectangular file into a variable size 2D list
#If there is any problems associated with the file (cannot open, file is empty, there is an error during the read process) 
#then the program will display an appropriate error message and repeatedly prompt the user for the name of the input file and attempt the file read process anew.
#return(refrence to a 2D list)

def fileRead():
    #create list
    list = []
    inputFileOK = False
    #repeatedly prompt the user to enter the file name if error occurs and file can not open propertly
    while(inputFileOK == False):
        try:
            inputFileName = input("Enter name of input file: ")
            #open file in reading mode
            inputFile = open(inputFileName,"r")
            print("Opening file", inputFileName, " for reading.")
            line = inputFile.readline()
            #displays error message for empty file
            if (line == EMPTY):
                print("%s is an empty file")
            else:
                currentRow = 0
                #reads the input file until the next line in the file is empty or just has a new line
                while(line != EMPTY and line!= NEWLINE):
                    list.append([]) #create a new row for the 2D list
                    currentColumn = 0
                    #reads each column of characters into the list until a new line has occured 
                    while(line[currentColumn] != NEWLINE ):
                        ch = line[currentColumn]
                        if(line[currentColumn] == " " or line[currentColumn] == "*" ):
                            #add * or space characters into the list 
                            list[currentRow].append(ch)
                        currentColumn += 1
                    currentRow +=1
                    #read the next line of input file
                    line = inputFile.readline()
            #close the input file
            inputFile.close()
        #exception handling for the file in case it can not open
        except IOError:
            print("Error: File", inputFileName, "could not be opened")
        else:
            print("Successfully read information from file", inputFileName)
            inputFileOK = True
        finally:
            print("Finished file input and output")
    return (list)

#getInitialWorld()
#function will:
#   prompt the user (quit or continue to the next turn: the option to toggle debugging won't be displayed but the program will react to this selection)
#return: reference to a list the initialized biosphere
def getInitalWorld():
    oldWorld =[]
    valid = False
    # repeatedly prompt the user to enter a valid choice until a valid choice has been made 
    while(valid == False):
        
        #display choices
        print("Choices for starting biospheres")
        print("(1) Empty") 
        print("(2) Single critter ") 
        print("(3) Single birth") 
        print("(4) Simple birth") 
        print("(5) Edgey testing") 
        print("(6) It's a complex world")
        print("(7) Input a file")
        
        #take user inputted choice
        choice = int(input("Selection: "))
        
        valid = True
        
        #a 2D list will be initialized according to user's choice  
        if(choice == 1):
            oldWorld = oneEmpty()
        elif(choice == 2):
            oldWorld = twoSingleCritter()
        elif(choice == 3):
            oldWorld = threeSingleBirth()
        elif(choice == 4):
            oldWorld = fourthSimpleBirth()
        elif(choice == 5):
            oldWorld = fifthCreateListEdgeCases()
        elif(choice == 6):
            oldWorld = sixthComplexCases()
        elif(choice == 7):
            oldWorld = fileRead()
        else:
            # if user choice not valid: change the flag and display an error message so that the user can input again
            valid = False
            print("Please print a number that is included in the range(1-7)")
        
    return oldWorld
        

#checkNeighborhood(int,int,reference to list)
#function features:
#   function will use the row and column of the 2D list bioshpere and see how many alive cells there are in the nieghborhood
#return int
def checkNeighborhood (r,c,oldWorld):
    aliveCounter = 0
    #iterate through the neighborhood of the located cell
    for i in range(r-1, r+2, 1):
        for j in range(c-1, c+2, 1):
            #check if neighborhood is in the range of the 2D list biosphere
            if i >= 0 and j >= 0 and i < len(oldWorld) and j < len(oldWorld[0]):
                #skip the located cell only check it's neighborhood and count the number of alive cells 
                if oldWorld[i][j] == "*" and (i != r or j != c):
                    aliveCounter += 1
    return aliveCounter


#getNextState(int,int,reference to list)
#function features:
#   function will check the state of the located cell and use the number of alive cells in the neighborhood to determine its next phase
#   returns the next state of the cell
#return char
def getNextState(r,c,oldWorld):
    #check the number of alive neighborhoods for the located cell
    aliveNeighbors = checkNeighborhood(r,c,oldWorld)
    #determine the state of the located cell
    #use the number of alive cells in the neighborhood to determine its next phase
    #If the an existing square in the old world contains a critter then the critter will continue living in the corresponding location in the new world if:There are either 2 or 3 neighbors.
    if oldWorld[r][c] == "*":
        if aliveNeighbors == 2 or aliveNeighbors == 3:
            ch = "*"
        else:
            ch = " "
            #if debug mode is on then print the row and column of the cell that will occur a death
            if(debugOn == True):
                print("<<<Critter death at %d and %d >>>" % (r,c ))
    elif oldWorld[r][c] == " ":
        #If the an existing square in the old world is empty then a birth may occur in the corresponding location in the new world if:There are exactly three neighbors in the old world.
        if aliveNeighbors == 3:
            ch = "*"
            if(debugOn == True):
                #if debug mode is on then print the row and column of the cell that will occur a birth
                print("<<<Critter born at %d and %d >>>" %(r,c ))
        else:
            ch = " "
    return ch

#getNewWorld(reference to a 2D list)
#function features:
#   create a new 2D list to represent the biosphere of the next phase 
#   check the next state of all locations in the old 2D list biosphere and pass it on to the new 2D list biosphere
#   return the new 2D list biosphere
#return: reference to a 2D list    
def getNewWorld(oldWorld):
    numRows =len(oldWorld)
    numCols = len(oldWorld[0])
    # make a NEW list with same diameter as oldWorld 
    newWorld = []
    for r in range (0, numRows, 1):
        newWorld.append([])
        for c in range (0, numCols, 1):
                newWorld[r].append(getNextState(r,c,oldWorld))
    return newWorld

#updateNewWorld(reference to a 2D list,reference to a 2D list)
#function features:
#   next phase of the biosphere-copy the new world biosphere into the old world
#   return the old 2D list biosphere
#return: reference to a 2D list   

def updateWorld(oldWorld,newWorld):
    numRows =len(oldWorld)
    numCols = len(oldWorld[0])
    for r in range (0, numRows, 1):
        for c in range (0, numCols, 1):
            oldWorld[r][c] = newWorld[r][c]
    return oldWorld




#################################################################
# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
#start()
#starting starting execution point of program
#determine if user wants to continue the game or quit the game
#count the number of turns of the simulation
def start():
    global debugOn
    
    quit = False
    turn = 0
    #initialize the user chosen biosphere
    oldWorld = getInitalWorld()
    #run the program until user chooses to quit
    while(quit == False):
        #get the next phase of biosphere
        newWorld = getNewWorld(oldWorld)
        #display both phases of biospheres and the turn number to screen
        display(turn,oldWorld,newWorld) 
        
        # prompt the user (quit or continue to the next turn: the option to toggle debugging won't be displayed but the program will react to this selection)
        choice = input("Hit enter to continue ('q' to quit): ")
        if(choice == "q" or choice =="Q"):
            quit = True
        if(choice == "d" or choice == "D"):
            debugOn = True
            print("<<< DEBUG messages ON! >>>")
        
        #copy the new world biosphere into the old world biosphere
        oldWorld = updateWorld(oldWorld,newWorld)
        turn +=1
start()


