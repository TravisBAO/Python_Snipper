

def selection_sort(list_under_test):
    list_length = len(list_under_test)
    for i in range(0, list_length - 1):
        temp_min_index = i
        for j in range(i + 1, list_length):
            if list_under_test[temp_min_index] > list_under_test[j]:
                temp_min_index = j
            else:
                pass
        temp_min = list_under_test[temp_min_index]
        list_under_test[temp_min_index] = list_under_test[i]
        list_under_test[i] = temp_min
        print("after loop " + str(i) + ", the list is " + str(list_under_test))
    print(list_under_test)


if __name__ == '__main__':
    testlist = [1500, 987, 725, 56, 89, 0, 34, 333, 34]
    selection_sort(testlist)
