# initializing all of the global variables that will be declared in
# each function of python

x = 0
y = 0
i = 0
step = 0
binary = 0
binary2 = 0
binary3 = 0
mainsteps = 0
searchsteps = 0
gameresets = 0
current_x = 0
current_y = 0
starting_x = -1
starting_y = 0

# checks that the user input is correct and resets the necessary
# global variables

def setParams(type, arrows, wumpi):

    global i
    global x
    global y
    global binary
    global binary2
    global binary3
    global mainsteps
    global searchsteps
    global step
    global gameresets

    if (gameresets == 0):

        if type > 2:
            type = 1
        elif type <= 0:
            type = 1
            print("Value error. The game will have non-moving wumpi")
            # why would we set game to type 0?
        if arrows <= 0:
            arrows = 1
            print("Value error. The agent has been given 1 arrow.")
        if wumpi <= 0:
            wumpi = 1
            print("Value error. The cave has spawned 1 wumpus.")
        gameresets = gameresets + 1
    else:

        #resets all the important values whenever a new game begins
        i = 0
        x = 0
        y = 0
        step = 0
        binary = 0
        binary2 = 0
        binary3 = 0
        mainsteps = 0
        searchsteps = 0

# this will be called to construct a blank 2d array that 
# the agent will be using as a map in the cave

def gridBuilder(x, y):

    grid = [[0 for i in range(x)] for j in range(y)]
    return grid

# this method will take the agent to the top left corner and find the size of the grid
# by counting over and down and measuring the amount of steps taken to reach each wall

def findGridSize(sensor):

    # agent begins by finding the top left corner, checking for gold, avoiding
    # pits, and killing wumpi along the way
    global step
    global binary2
    global y
    global x
    global grid
    global current_x
    global current_y
    global i
    global starting_x
    global starting_y

    if (binary2 == 1):
        step = step + 1
        binary2 = 0
        return "G"
    elif(binary2 == 0):
        if step == 0:
            if sensor != "U":
                starting_x = starting_x + 1
                return "N"
            elif sensor == "U" or sensor == "UB":
                i = i + 1
                binary2 = 1
                return 'W'
        elif step == 1:
            if sensor != "U":
                starting_y = starting_y + 1
                return "W"
            elif sensor == "U" or "UB":
                i = i + 1
                binary2 = 1
                x = x + 1
                return "E"
        elif step == 2:
            if sensor != "U":
                x = x + 1
                return "E"
            elif sensor == "U" or "UB":
                binary2 = 1
                i = i + 1
                y = y + 1
                return "S"
        elif step == 3:
            if sensor != "U":
                y = y + 1
                return "S"
            elif sensor == "U" or "UB":
                i = i + 1
                x = x - 1
                y = y - 1
                grid = gridBuilder(x, y)
                print(x)
                print(y)
                print(starting_x, starting_y)
                current_x = x
                current_y = y
                print (current_x, current_y)
                return 'G'

# this is the general search method the agent will be using, it will iterate 
# through the grid one row at a time until it reaches the gold

def beginSearch(sensor):
    # values to record what postion the agent is in, in the grid
    global searchsteps
    global binary3
    global current_x
    global current_y
    global starting_x
    global starting_y

    if(sensor != 'G' or sensor != 'UG'):
        #print(current_x, current_y)
        if (binary3 == 2):
            searchsteps = searchsteps + 1
            binary3 = 1
            return 'SN'
        elif(binary3 == 0):
            if (current_y > 0 and searchsteps == 0):
                current_y = current_y - 1
                print ('W')
                print (current_x, current_y)
                return 'W'
            elif(current_y == 0 and searchsteps == 0):
                if(current_x > 0):
                    current_x = current_x - 1
                    binary3 = 2
                    print ('N')
                    print (current_x, current_y)
                    return 'N'
                elif(current_x == 0):
                    return('G')
        elif(binary3 == 1):
            if(current_y < x and searchsteps == 1):
                current_y = current_y + 1
                print ('E')
                print (current_x, current_y)
                return 'E'
            elif(current_y == x and searchsteps == 1):
                if(current_x > 0):
                    current_x = current_x - 1
                    print ('N')
                    print (current_x, current_y)
                    searchsteps = 0
                    binary3 = 0
                    return('N')
                elif(current_x == 0):
                    return 'G'
    elif(sensor == 'G' or sensor == 'UG'):
        print("gold found!")
        return 'G'

# this will have the agent return to the starting position 
# it was dropped in the cave 

def returnHome(sensor):
    global current_x
    global current_y
    global starting_x
    global starting_y
    
    while True:
        if(current_x < starting_x):
            print("Starting x is" , starting_x)
            current_x = current_x + 1
            print (current_x, current_y)
            print('S')
            return 'S'
        elif(current_x > starting_x):
            print("Starting x is" , starting_x)
            current_x = current_x - 1
            print(current_x, current_y)
            print('N')
            return 'N'
        elif(current_x == starting_x):
            if(current_y < starting_y):
                print(current_x, current_y)
                print('E')
                current_y = current_y + 1
                return 'E'
            elif(current_y > starting_y):
                current_y = current_y - 1
                print(current_x, current_y)
                print('W')
                return 'W'
            elif(current_y == starting_y):
                print(current_x, current_y)
                print ('C')
                binary = 1
                return 'C'

# main function that calls each new step/goal for the agent

def getMove(sensor):

    # will be used to increment through the agent's searching process
    global mainsteps
    global grid

    # keeps track of the previous move of the agent
    global lastmove
    global current_x
    global current_y
    # used to switch on and off whether a new step will begin
    global binary
    global i

    if(binary == 1):
        mainsteps = mainsteps + 1
        binary = 0
        return 'G'
    elif(binary == 0):
        if (mainsteps == 0):
            if(i != 4):
                return findGridSize(sensor)
            elif(i == 4):
                binary = 1
                return 'G'
        elif (mainsteps == 1):
            if(sensor != 'G'):
                return beginSearch(sensor)
            elif(sensor == 'G'):
                binary = 1
                print('gold found')
                return 'G'
        elif (mainsteps == 2):
            return returnHome(sensor)
            




 
