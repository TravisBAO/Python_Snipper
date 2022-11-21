inputNumber = 1
isPrime = False
primeList = []

while (inputNumber <= 100):
    divideNumber = 2
    if inputNumber == 2: # check 2 separtely
        primeList.append(inputNumber)
    
    while (divideNumber < inputNumber):  
        result = inputNumber % divideNumber
        if result == 0: #The number is not a prime
            isPrime = False
            break
        divideNumber += 1
        isPrime = True        
    if isPrime:    
        primeList.append(inputNumber)

    inputNumber += 1
print(primeList)    
		

  
