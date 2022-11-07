import sys
import copy
import time

class bottle:
    def __init__(self,water:list):
        water.reverse()
        self.water = water
        self.completed = False

    def __eq__(self, other):
        return self.water == other.water and self.completed == other.completed

    def printShape(self):
        print("---")
        counter = 0
        tmp = copy.deepcopy(self.water)
        for i in range(4-len(self.water)):
            print("|*|")   
        for i in range(len(self.water)):
            print("|"+tmp.pop()+"|")  
        print("---")
    def isCompleted(self):
        return self.completed

    def checkCompletion(self):
        if len(self.water) == 4:
            if self.water[0] == self.water[1] and self.water[0] == self.water[2] and self.water[0] == self.water[3]:
                return True
        return False

    def setComplete(self):
        self.completed = True

    def getAmount(self):
        return len(self.water)
    
    def getTopColor(self): 
        # return None if size = 0, else return top color
        if (len(self.water) == 0):
            return None
        return self.water[-1]

    def countTopColor(self): 
        # return None if size = 0, else return the amount of color is the same in the top of bottle
        if len(self.water) == 0:
            return 0
        elif len(self.water) == 1:
            return 1
        top = self.water[-1]
        for i in range(2,len(self.water)+1):
            if self.water[-i] != top:
                return i-1
        return len(self.water)
    
    def removeWater(self,n):
        if n > len(self.water):
            self.printShape()
        for i in range(n):
            self.water.pop()
    
    def addWater(self,n,color):
        for i in range(n):
            self.water.append(color)

class game:
    def is_valid_value(self,char):
        if ( char == '*' or #empty
            char == 'O' or #orange
            char == 'B' or #blue
            char == 'R' or #red
            char == 'C' or #cyan
            char == 'G' or #gray
            char == 'Y' or #yellow
            char == 'P'):
            return True
        else:
            return False
    def __init__(self,filename,level):
        self.space = []
        level_found = False
        if level < 1 or level > 20:
            print ("ERROR: Level "+str(level)+" is out of range")
            sys.exit(1)
        else:
            file = open(filename,'r')
            self.n = 0 # number of bottles
            for line in file:
                row = []
                if not level_found:
                    if  "Level "+str(level) == line.strip():
                        level_found = True
                else:
                    if line.strip() != "":
                        row = []
                        for c in line:
                            # print(c)
                            if c != '\n' and self.is_valid_value(c):
                                if c != '*':
                                    row.append(c)
                                continue
                            elif c == '\n': #jump to next row when newline
                                self.n+=1
                                continue
                            else:
                                print("ERROR: Level "+str(level)+" has invalid value "+c)
                                sys.exit(1)                  
                        self.space.append(bottle(row))
                    else:
                        break

def printState(space):
    for i in space:
        i.printShape()

def pourWater(firstBot,secondBot):
    color= firstBot.getTopColor()
    counter = firstBot.countTopColor()
    firstBot.removeWater(counter)
    secondBot.addWater(counter,color)

def canPour(firstBot,secondBot): 
    color1 = firstBot.getTopColor()
    counter = firstBot.countTopColor()
    if color1 == None or counter == 0: # size = 0
        return False
    color2 = secondBot.getTopColor()
    if color1 != color2 and color2 != None: # khac mau top color nen khong chuyen duoc
        return False
    secondBotAmount = secondBot.getAmount()
    if (secondBotAmount < 4 and secondBotAmount+counter<=4): # check if we can remove Water in first bottle and pour to the other
        return True
    return False

def isCompleted(space):
    for i in space:
        if i.getAmount() == 0:
            continue
        if i.isCompleted() == False:
            return False
    return True

def dfs_solve(space):
    start = time.perf_counter()
    counter = 0
    visited = []
    moves = []
    queue = [((space,moves),0)]
    visited.append(space)
    repeated_nodes = 0
    thresh = 100000
    while len(queue)>0:
        currentState = queue.pop()
        currentSpace = currentState[0][0]
        currentCounter = currentState[1]
        if currentCounter > thresh:
            continue
        if isCompleted(currentSpace):
            end = time.perf_counter()
            return currentState[0][0],currentState[0][1], len(visited)+len(queue),len(visited),repeated_nodes,end-start
            # return goal state,moves, states reached = len(visited) + len(queue),visited = len(visited), repeated_nodes, time = end - start

        for i in range(0,len(currentSpace)):

            if currentSpace[i].isCompleted():
                continue
            for j in range(0,len(currentSpace)):
                if currentSpace[j].isCompleted():
                    continue
                if i != j:
                    currentMoves = copy.deepcopy(currentState[0][1])
                    temp_space = copy.deepcopy(currentSpace)
                    if not canPour(temp_space[i],temp_space[j]):
                        continue
                    pourWater(temp_space[i],temp_space[j])
                    if temp_space[j].checkCompletion():
                        temp_space[j].setComplete()
                    # print(i,j)
                    if temp_space not in visited:
                        currentCounter+=1
                        currentMoves.append([i,j])
                        queue.append(((temp_space,currentMoves),currentCounter))
                        visited.append(temp_space)
                        
                    else:
                        repeated_nodes+=1
    print("Cant solve")
    end = time.perf_counter()
    return [],[], len(visited)+len(queue),len(visited),repeated_nodes,end-start

def bfs_solve(space):
    start = time.perf_counter()
    visited = []
    moves = []
    queue = [(space,moves)]
    visited.append(space)
    repeated_nodes = 0
    while len(queue)>0:
        currentState = queue.pop(0)
        currentSpace = currentState[0]
        if isCompleted(currentSpace):
            end = time.perf_counter()
            return currentState[0],currentState[1], len(visited)+len(queue),len(visited),repeated_nodes,end-start
        for i in range(0,len(currentSpace)):
            if currentSpace[i].isCompleted():
                continue
            for j in range(0,len(currentSpace)):
                if currentSpace[j].isCompleted():
                    continue
                if i != j:
                    currentMoves = copy.deepcopy(currentState[1])
                    temp_space = copy.deepcopy(currentSpace)
                    if not canPour(temp_space[i],temp_space[j]):
                        continue
                    pourWater(temp_space[i],temp_space[j])
                    if temp_space[j].checkCompletion():
                        temp_space[j].setComplete()
                    # print(i,j)
                    if temp_space not in visited:
                        currentMoves.append([i,j])
                        queue.append((temp_space,currentMoves))
                        visited.append(temp_space)
                    else:
                        # print(i,j)
                        repeated_nodes+=1
    print("Cant solve")
    end = time.perf_counter()
    return [],[], len(visited)+len(queue),len(visited),repeated_nodes,end-start

#-----------------------------------------------------------------------#
def write_File(moves, all_nodes, visited_nodes, repeated_nodes, time_run, filename, level):
    stringcopy = "Level " + str(level) + "\n"
    stringcopy += "Moves: " + str(len(moves)) + "\n"
    stringcopy += "Number of states have been reached: " + str(all_nodes) + "\n"
    stringcopy += "Number of states have been visited: " + str(visited_nodes) + "\n"
    stringcopy += "Number of duplicated states: " + str(repeated_nodes) + "\n"
    stringcopy += "Time for searching: " + str(time_run) + "\n"
    stringcopy += "*****************************************************\n"
    file = open(filename, "a")
    file.write(stringcopy)
    file.close()
#-----------------------------------------------------------------------#
def run(fileread, filewrite):
  level = 1
  while level <= 20:
    g = game(fileread,level)
    print("Solving testcase " + str(level) + ".........")
    last_state, moves, all_nodes, visited_nodes, repeated_nodes, time_run = dfs_solve(g.space)
    if moves == []:
      file = open(filewrite, "a")
      file.write("Testcase is fail\n")
      file.close()
      write_File(moves, all_nodes, visited_nodes, repeated_nodes, time_run, filewrite, level)
    else:
      write_File(moves, all_nodes, visited_nodes, repeated_nodes, time_run, filewrite, level)
    print("Done")
    level += 1
  return level
#-----------------------------------------------------------------------#
# count = run("./input.txt", "./dfs-result.txt")
# print("Successfully!!!")

