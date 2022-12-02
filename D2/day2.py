resultWin = 0
resultOption = 0  

def winner(opponentInput, myInput):

    global resultWin
    global resultOption

    match opponentInput:
        case 'A':
            match myInput:
                case 'X':
                    resultWin += 3
                    resultOption += 1
                case 'Y':
                    resultWin += 6
                    resultOption += 2
                case 'Z':
                    resultWin += 0
                    resultOption += 3
                case _:
                    print('impossible')           
        case 'B':
            match myInput:
                case 'X':
                    resultWin += 0
                    resultOption += 1
                case 'Y':
                    resultWin += 3
                    resultOption += 2
                case 'Z':
                    resultWin += 6
                    resultOption += 3
                case _:
                    print('impossible')      
        case 'C':
            match myInput:
                case 'X':
                    resultWin += 6
                    resultOption += 1
                case 'Y':
                    resultWin += 0
                    resultOption += 2
                case 'Z':
                    resultWin += 3
                    resultOption += 3
                case _:
                    print('impossible')      
        case _:
            print('impossible')

def winnerPart2(opponentInput, myInput):

    global resultWin
    global resultOption

    match opponentInput:
        case 'A':
            match myInput:
                case 'X':
                    resultWin += 0  
                    resultOption += 3
                case 'Y':
                    resultWin += 3
                    resultOption += 1
                case 'Z':
                    resultWin += 6
                    resultOption += 2
                case _:
                    print('impossible')           
        case 'B':
            match myInput:
                case 'X':
                    resultWin += 0
                    resultOption += 1
                case 'Y':
                    resultWin += 3
                    resultOption += 2
                case 'Z':
                    resultWin += 6
                    resultOption += 3
                case _:
                    print('impossible')      
        case 'C':
            match myInput:
                case 'X':
                    resultWin += 0
                    resultOption += 2
                case 'Y':
                    resultWin += 3
                    resultOption += 3
                case 'Z':
                    resultWin += 6
                    resultOption += 1
                case _:
                    print('impossible')      
        case _:
            print('impossible')



with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        inputsArray = line.split() 
        winnerPart2(inputsArray[0], inputsArray[1])
print(resultWin + resultOption )