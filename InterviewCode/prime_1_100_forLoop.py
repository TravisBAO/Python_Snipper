PrimeList = []
isPrime = False

for i in range(1, 101):
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
        else:
            isPrime = True
    if isPrime:
        PrimeList.append(i)
print(PrimeList)