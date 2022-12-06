from collections import deque
with open('input.txt') as f:
    while True:
        line = f.readline().strip() 
        if not line:
            break
        myElements = deque([]) 
         
        for count, value in enumerate([*line]): 
            print(myElements)
            if len(myElements)==14 and len(myElements) == len(set(myElements)):
                print(count)
                break
            elif (value not in myElements): 
                myElements.append(value)
                if (len(myElements)>14):
                    myElements.popleft()
            else :
                myElements.popleft()
                myElements.append(value)
           
        # print([*line])