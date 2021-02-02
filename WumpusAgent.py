# import random

# stack that keeps track of last move of the agent
lastmove = []
# stack that keeps track of the the last sensory inputs
sensorstack = []
# stack that keeps track of all moves so you can find your way back to the
# beginning
allmoves = []
# stack that gives directions for avoiding and marking a pit after moving N
pitavoidN = []
# stack that gives directions for avoiding and marking a pit after moving E
pitavoidE = []
# stack that gives directions for avoiding and marking a pit after moving S
pitavoidS = []
# stack that gives directions for avoiding and marking a pit after moving W
pitavoidW = []

x = 0
y = 0
step = 0
binary = 0
binary2 = 0
mainsteps = 0

def setParams(type, arrows, wumpi):
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

# trying to create a representation of what the agent has discovered so far
def gridBuilder(x, y):

    grid = [[0 for i in range(x)] for j in range(y)]
    return grid

def lastMove(move):
    return lastmove.append(move)

def allMoves(move):
    return allmoves.append(move)

def findGridSize(sensor):

    # agent begins by finding the top left corner, checking for gold, avoiding
    # pits, and killing wumpi along the way
    global step
    global binary2
    global y
    global x
    global grid

    if (binary2 == 1):
        step = step + 1
        binary2 = 0
        return "G"
    elif(binary2 == 0):

        if step == 0:

            if sensor != "U":
                return "N"
            elif sensor == "U" or "UB":
                binary2 = 1
                return 'G'

        elif step == 1:
            if sensor != "U":
                return "W"

            elif sensor == "U" or "UB":
                binary2 = 1
                return "G"
        elif step == 2:

            if sensor != "U":
                x = x + 1
                return "E"
            elif sensor == "U" or "UB":
                binary2 = 1
                return "G"
        elif step == 3:

            if sensor != "U":
                y = y + 1
                return "S"
            elif sensor == "U" or "UB":
                binary2 = 2
                grid = gridBuilder(x, y)
                print(grid)
                return "G"


def getMove(sensor):

    # will be used to increment through the agent's searching process
    global mainsteps
    global grid
    # keeps track of every (directional) move made by the agent.
    # Will be used to retrace the steps of the agent back to the
    # starting position
    global allmoves

    # keeps track of the previous move of the agent
    global lastmove

    # used to switch on and off whether a new step will begin
    global binary


    return findGridSize(sensor)

































    # r1 = random.randint(0, 3)
    # r2 = random.randint(0, 2)
    # a more basic attempt that will allow the agent to do basic pit and wumpus
    # avoidance while moving randomly.
    # if (binary == 0):
    #    if (sensor == ''):
    #        if (r1 == 0):
    #            lastMove('N')
    #            allMoves('N')
    #            return 'N'
    #        elif (r1 == 1):
    #            lastMove('E')
    #            allMoves('E')
    #            return 'E'
    #        elif (r1 == 2):
    #            allMoves('S')
    #            return 'S'
    #        elif (r1 == 3):
    #            lastMove('W')
    #            allMoves('W')
    #            return 'W'
    #    elif (sensor == 'G'):
    #        return 'G'
    #        binary = 1
    #    elif ((sensor == 'B') and lastmove.pop() == 'N'):
    #        lastMove('S')
    #        allMoves('S')
    #        return 'S'
    #    elif ((sensor == 'B') and lastmove.pop() == 'E'):
    #        lastMove('W')
    #        allMoves('W')
    #        return 'W'
    #    elif ((sensor == 'B') and lastmove.pop() == 'S'):
    #        return 'N'
    #        lastMove('N')
    #        allMoves('N')
    #    elif ((sensor == 'B') and lastmove.pop() == 'W'):
    #        return 'E'
    #        lastMove('E')
    #        allMoves('E')
    #    elif ((sensor == 'S') and lastmove.pop() == 'N'):
    #        if (r2 == 0):
    #            return 'SN'
    #        elif (r2 == 1):
    #            return 'SW'
    #        elif (r2 == 2):
    #            return 'SE'
    #    elif ((sensor == 'S') and lastmove.pop() == 'E'):
    #        if (r2 == 0):
    #            return 'SN'
    #        elif (r2 == 1):
    #            return 'SE'
    #        elif (r2 == 2):
    #            return 'SS'
    #    elif ((sensor == 'S') and lastmove.pop() == 'S'):
    #        if (r2 == 0):
    #            return 'SS'
    #        elif (r2 == 1):
    #            return 'SE'
    #        elif (r2 == 2):
    #            return 'SW'
    #    elif ((sensor == 'S') and lastmove.pop() == 'W'):
    #        if (r2 == 0):
    #            return 'SW'
    #        elif (r2 == 1):
    #       elif (r2 == 2):
    #            return 'SN'
    #    else:
    #        if (r1 == 0):
    #            return 'N'
    #            lastMove('N')
    #            allMoves('N')
    #        elif (r1 == 1):
    #            return 'E'
    #            lastMove('E')
    #            allMoves('E')
    #        elif (r1 == 2):
    #            return 'S'
    #            lastMove('S')
    #            allMoves('S')
    #        elif (r1 == 3):
    #            return 'W'
    #            lastMove('W')
    #            allMoves('W')
    # elif (binary == 1):
    #    return allmoves.pop()
    #    if not allmoves:
    #        return 'C'



    # global step
    # global x
    # global y

    # agent begins by finding the top left corner, checking for gold, avoiding
    # pits, and killing wumpi along the way

    # if (binary == 1):
    #    step = step + 1
    #    binary = 0
    # elif(binary == 0):
    #    if step == 0:
    #        if sensor != "U":
    #            return "N"
    #        elif sensor == "U" or sensor == "UB":
    #            return "W"
    #            binary = 1

    #    elif step == 1:
    #        if sensor != "U":
    #            return "W"
    #        elif sensor == "U" or "UB":
    #            return "E"
    #            binary = 1
    #    elif step == 2:

    #        if sensor != "U":
    #            return "E"
    #            x = x + 1
    #        elif sensor == "U" or "UB":
    #            return "S"
    #            binary = 1
    #    elif step == 3:

    #        if sensor != "U":
    #            return "S"
    #            y = y + 1
    #        elif sensor == "U" or "UB":
    #            return "S"
    #            binary = 1
    #            grid = gridBuilder(x, y)




