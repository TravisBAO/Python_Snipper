secondList = []
isPrime2 = False
for i in range(1, 101):
    if i == 1:
        continue
    if i == 2:
        secondList.append(i)
        continue
    for j in range(2, i):
        if i % j == 0:
            isPrime2 = False
            break
        else:
            isPrime2 = True
    if isPrime2:
        secondList.append(i)

print(secondList)