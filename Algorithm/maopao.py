def qiguai(listundertest): # todo: 写的一个奇怪的算法，尝试看一下问题，同时看一下复杂度
    listlength = len(listundertest)
    print("length of the list under test is " + str(listlength))
    print(listundertest)

    for i in range(listlength):
        # print(str(i) + " is " + str(listundertest[i]))
        j = 1
        for j in range(1, listlength):
            print("current i == " + str(i))
            print("current j == " + str(j))
            if listundertest[i] > listundertest[j]:
                temp = listundertest[j]
                listundertest[j] = listundertest[i]
                listundertest[i] = temp
                print(listundertest)
    
    print(listundertest)


def maopao(listundertest):
    listlength = len(listundertest)
    print("length of the list under test is " + str(listlength) + "\n")
    print(str(listundertest) + "\n")

    for i in range(listlength - 1): #  这个for 决定列表中有哪些元素可以参与对比，随着循环的进行，参加对比的元素列表越来越短，体现在下一行的 "listlength-1-i".也要注意i本身不参与值对比的计算
        for j in range (listlength - 1 - i):
            if listundertest[j] > listundertest[j + 1]:
                temp = listundertest[j + 1]
                listundertest[j + 1] = listundertest[j]
                listundertest[j] = temp
                # listundertest[j], listundertest[j + 1] = listundertest[j + 1], listundertest[j] 

        print("The " + str(i + 1) + " round is done! And the current list is " + str(listundertest))
        print("\n")

    print("The final list is ------> " + str(listundertest))
    

if __name__ == '__main__':
    testlist = [1500, 987, 725, 56, 89, 0, 34, 333, 34]
    maopao(testlist)
