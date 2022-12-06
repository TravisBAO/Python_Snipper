listUnderTest = [12, 34, 3, 45, 89, 333, 909, 23, 10, 35]
print(listUnderTest)

listLength = len(listUnderTest)

for i in range(listLength - 1):
    minIndex = i
    for j in range(i, listLength):
        if listUnderTest[minIndex] > listUnderTest[j]:

            tempValue = listUnderTest[minIndex]
            listUnderTest[minIndex] = listUnderTest[j]
            listUnderTest[j] = tempValue
    #         minIndex = j
    # tempValue = listUnderTest[minIndex]
    # listUnderTest[minIndex] = listUnderTest[i]
    # listUnderTest[i] = tempValue
print(listUnderTest)
