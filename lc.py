listunderSort = [1,2,4,6,7,44,4,333,234,26,45,678,12,56]
print("The initial one is" + str(listunderSort))

lengthOfList = len(listunderSort)
for i in range(lengthOfList - 1):
    for j in range(lengthOfList - 1 - i):
        if listunderSort[j] < listunderSort[j+1]:
            listunderSort[j], listunderSort[j+1] = listunderSort[j+1], listunderSort[j]

print("The final one is" + str(listunderSort))

for x in range(6):
    print(x)

