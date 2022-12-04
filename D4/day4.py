totalOverlaps = 0

def calculateOverlaps(myLines):
    myFirstElement = myLines[0]
    mySecondElement = myLines[1]

    myFirstElementCharacters = myFirstElement.split('-')
    firstElementArray = list(range(int(myFirstElementCharacters[0]), int(myFirstElementCharacters[1]) + 1))
    
    mySecondElementCharacters = mySecondElement.split('-')
    secondElementArray = list(range(int(mySecondElementCharacters[0]), int(mySecondElementCharacters[1]) + 1))

    checkAll = all(item in firstElementArray for item in secondElementArray)
    checkAll2 = all(item in secondElementArray for item in firstElementArray)

    checkAny = any(item in firstElementArray for item in secondElementArray)
    checkAny2 = any(item in secondElementArray for item in firstElementArray)


    if checkAny or checkAny2 is True :
        return 1
    else :
        return 0

with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        myLines = line.strip().split(',')
        totalOverlaps += calculateOverlaps(myLines)
    print(totalOverlaps)
        