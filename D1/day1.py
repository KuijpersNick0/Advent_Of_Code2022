newMaxCalories0 = 0
maxCalories0 = 0
maxCalories1 = 0
maxCalories2 = 0

with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if (line == '\n') :
            if (newMaxCalories0 > maxCalories0) :
                maxCalories2 = maxCalories1
                maxCalories1 = maxCalories0
                maxCalories0 = newMaxCalories0

            elif (newMaxCalories0 > maxCalories1):
                maxCalories2 = maxCalories1
                maxCalories1 = newMaxCalories0

            elif (newMaxCalories0 > maxCalories2):
                maxCalories2 = newMaxCalories0

            newMaxCalories0 = 0
        else :
            newMaxCalories0 += int(line)
    print(maxCalories0 + maxCalories1 + maxCalories2)


