def insertion_sort(test_list):

    for i in range(1, len(test_list)):
        temp_value = test_list[i]
        j = i - 1
        while j >= 0 and temp_value < test_list[j]:
            test_list[j+1] = test_list[j]
            j -= 1
        test_list[j + 1] = temp_value
    print(test_list)


if __name__ == '__main__':
    testlist = [1, 987, 725, 56, 89, 0, 34, 333, 34]
    insertion_sort(testlist)
