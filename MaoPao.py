def maopao(listundertest):     
    listlength = len(listundertest)     
    print("length of the list under test is " + str(listlength) + "\n")     
    print(str(listundertest) + "\n")     
    for i in range(listlength - 1): #第一个循环不参与值的排序         
        for j in range (listlength - 1 - i):             
            if listundertest[j] > listundertest[j + 1]:                 
                temp = listundertest[j + 1]                 
                listundertest[j + 1] = listundertest[j]                 
                listundertest[j] = temp         
        print("The " + str(i + 1) + " round is done! And the current list is " + str(listundertest))         
    print("\n")     
    print("The final list is ------> " + str(listundertest))      
    
if __name__ == '__main__':     
    testlist = [1500, 987, 725, 56, 89, 0, 34, 333, 34]     
    maopao(testlist)