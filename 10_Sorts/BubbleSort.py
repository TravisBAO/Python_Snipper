def qiguai(list_under_test): # todo: 写的一个奇怪的算法，尝试看一下问题，同时看一下复杂度
    list_length = len(list_under_test)
    print("length of the list under test is " + str(list_length))
    print(list_under_test)

    for i in range(list_length):
        # print(str(i) + " is " + str(list_under_test[i]))
        j = 1
        for j in range(1, list_length):
            print("current i == " + str(i))
            print("current j == " + str(j))
            if list_under_test[i] > list_under_test[j]:
                temp = list_under_test[j]
                list_under_test[j] = list_under_test[i]
                list_under_test[i] = temp
                print(list_under_test)
    
    print(list_under_test)


def bubble_sort(list_under_test):
    list_length = len(list_under_test)
    print("length of the list under test is " + str(list_length) + "\n")
    print(str(list_under_test) + "\n")

    for i in range(list_length - 1):
        # 上面这个for 决定列表中有哪些元素可以参与对比，随着循环的进行，参加对比的元素列表越来越短，
        # 体现在下一行的 "list_length-1-i".也要注意i本身不参与值对比的计算
        for j in range(list_length - 1 - i):
            if list_under_test[j] > list_under_test[j + 1]:
                temp = list_under_test[j + 1]
                list_under_test[j + 1] = list_under_test[j]
                list_under_test[j] = temp

        print("The " + str(i + 1) + " round is done! And the current list is " + str(list_under_test))
        print("\n")

    print("The final list is ------> " + str(list_under_test))
    

if __name__ == '__main__':
    testlist = [1500, 987, 725, 56, 89, 0, 34, 333, 34]
    bubble_sort(testlist)
