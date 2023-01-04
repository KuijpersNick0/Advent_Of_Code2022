tempAdd = 0  
space = 70000000
toFree = 30000000
 
def findCD(myElements):
    if myElements[0:6] == ['$', ' ', 'c', 'd', ' ', '.']:
        return False
    elif myElements[0:4] == ['$', ' ', 'c', 'd' ]:
        return True
    else:
        return False

def findCommand(line):
    myElements = [*line] 
    if myElements[0]=='$':
        return True
    else:
        return False    

def findLS(line):
    myElements = [*line]    
    if myElements[0:4]==['$', ' ', 'l', 's']:
        return True
    else :
        return False

def checkDir(line):
    myElements = [*line]    
    if myElements[0:3]==['d', 'i', 'r']:
        return True
    else :
        return False 

def findCdUp(myElements ): 
    if myElements[0:6] == ['$', ' ', 'c', 'd', ' ', '.']:  
        return True
    else :
        return False

class Node:
    def __init__(self, directory, parent, children=[], size=0):
        self.directory = directory   
        self.files = []  
        self.children = []
        self.hasChildren = False
        self.size=0
        self.parent = parent
        

    def __str__(self) -> str:
        return print(self.files)

    def getDir(self):
        return self.directory

    def getChildren(self):
        return self.children

    def getParent(self):
        return self.parent

    def addFiles(self, file):
        self.files.append(int(file))
    
    def addChild(self, node):
        self.children.append(node)

    def addSize(self):
        self.size += 1

    def getAllChilds(self):
        allChilds = []
        if self.hasChildren:
            for child in self.children:
                allChilds.append(child)
                if child.hasChildren: 
                    allChilds = allChilds + child.getAllChilds()
        return allChilds  

    def getFiles(self):
        res=0
        for file in self.files:
            res += file
        return res

    def getTotalFiles(self):
        res = self.getFiles()
        for child in self.children:
            res +=  child.getTotalFiles()
        return res

def displayNodes(node, indent=''):
    def print_node(node, indent):
        print(indent + node.directory)
        for file in node.files:
            print(indent + '  ' + str(file))
        for child in node.children:
            print_node(child, indent + '  ')
    print_node(node, indent)

def calculateSum(node, maxSize): 
    total = 0
    for child in node.children:
        if child.getTotalFiles() < maxSize:
            total += child.getTotalFiles()
        total += calculateSum(child, maxSize)
    return total

def findSmallestPossible(node):
    allChildren = node.getAllChilds()
    freeSpace = space - node.getTotalFiles()
    spaceRequiredForUpdate = toFree - freeSpace 
    
    currentSmallestFolder = node

    for child in allChildren:
        if child.getTotalFiles() > spaceRequiredForUpdate:
            if child.getTotalFiles() < currentSmallestFolder.getTotalFiles():
                currentSmallestFolder = child

    return currentSmallestFolder.getTotalFiles()

with open('input.txt') as f:
    global cwd
    
    rootNode = Node(directory='/', parent=None) 
    while True:
        lines = f.readlines()
        if not lines:
            break
        for i in range(len(lines)):
            myElements = [*lines[i].strip()] 
            if (findCD(myElements) == True):
                myDir = ''.join([str(elem) for elem in myElements[5:]])   
                if (myDir == '/'):
                    cwd = rootNode
                else:
                    for child in cwd.children:
                        if (myDir == child.getDir()):
                            cwd = child                     
                if (findLS(lines[i+1])==True):
                    k = 2 
                    while (((i+k)<len(lines)) and findCommand(lines[i+k])==False): 
                        myTwoElements = lines[i+k].split() 
                        if (checkDir(lines[i+k]) == True): 
                            newNode = Node(directory= myTwoElements[1], parent=cwd)   
                            cwd.addChild(newNode)  
                            cwd.addSize()
                            cwd.hasChildren = True
                        else : 
                            cwd.addFiles(myTwoElements[0])   
                            cwd.hasChildren = True
                        k+=1  
            if (findCdUp(myElements)==True and cwd.parent != None):  
                cwd = cwd.parent  
        
    displayNodes(rootNode)
    tempAdd = calculateSum(rootNode, 100000)  
    print(tempAdd)
    test = findSmallestPossible(rootNode)
    print(test)