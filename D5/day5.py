from collections import deque

crates = []
crateNr = []
commands = []
myAmount = 0
myStart = 0
myDestination = 0
myCrateDict = {} 

#Don't look at this very ugly

def createMyOrderDict(crates, crateNr):
    global myCrateDict 
    for count, value in enumerate(crateNr):
        for count2, value2 in enumerate(crates):
            if crates[count2][count] == '':
                pass
            else:
                if value in myCrateDict : 
                    myCrateDict[value].append([crates[count2][count]]) 
                else: 
                    myCrateDict[value] = deque([crates[count2][count]])


def moveCrates(commands): 

    def moveIt(myAmount, myStart, myDestination):
        myAmount = int(myAmount)
        # while myAmount > 0 :   
        #     toBeMoved =  myCrateDict[myStart].popleft()
        #     myCrateDict[myDestination].appendleft(toBeMoved)
        #     myAmount-=1  
        toBeMoved = []
        while myAmount > 0 :
            toBeMoved.append(myCrateDict[myStart].popleft())  
            myAmount-=1  
        for count, value in enumerate(toBeMoved):  
            myCrateDict[myDestination].appendleft(toBeMoved[-count-1])

    for count, value in enumerate(commands):
        myAmount = value.split()[1]
        myStart = value.split()[3]
        myDestination = value.split()[5]
        moveIt(myAmount, myStart, myDestination)


    return 0

with open('input.txt') as f:
    while True:
        lines = f.readlines()
        if not lines:
            break
        for line in lines[:8]:
            n = 4
            myLine = [line[i:i+n].strip() for i in range(0, len(line), n)]
            crates.append(myLine)
        
        for line in lines[8].split():
            crateNr.append(line)
        
        for line in lines[10:]:
            commands.append(line.strip())

        createMyOrderDict(crates, crateNr)
        moveCrates(commands)
    

    # print(crates)
    # print(crateNr)
    # print(commands)

    print(myCrateDict)
 