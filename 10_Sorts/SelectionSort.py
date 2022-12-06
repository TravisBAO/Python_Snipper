listUnderTest = [1500, 987, 725, 56, 89, 0, 34, 333, 34]
print("The original list is " + str(listUnderTest))
listLength = len(listUnderTest)

for i in range(listLength - 1):
    minIndex = i
    for j in range(i + 1, listLength):
        if listUnderTest[minIndex] > listUnderTest[j]:
            minIndex = j
    listUnderTest[minIndex], listUnderTest[i] = listUnderTest[i], listUnderTest[minIndex]
    
print("The final list is " + str(listUnderTest))            
