listUnderTest = [12,34,3, 45,89, 333, 909, 23, 10, 35]
print("The original list is " + str(listUnderTest))
listLength = len(listUnderTest)

for i in range(listLength - 1):
    minIndex = i
    for j in range (i + 1, listLength):
        if listUnderTest[minIndex] > listUnderTest[j]:
            minIndex = j
    listUnderTest[minIndex], listUnderTest[i] = listUnderTest[i], listUnderTest[minIndex]
    
print("The final list is " + str(listUnderTest))            
