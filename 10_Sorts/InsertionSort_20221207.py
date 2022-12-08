def insertion_sort(test_list):

    # Traverse through 1 to len(test_list)
    for i in range(1, len(test_list)):
        target_value = test_list[i]

        # Move elements of test_list[0..i-1],
        # that are greater than target_value,
        # to one position ahead of their current position
        j = i-1
        while j >= 0 and target_value < test_list[j]:
            test_list[j + 1] = test_list[j]
            j -= 1
        test_list[j + 1] = target_value

    print(test_list)


if __name__ == '__main__':
    testlist = [1, 987, 725, 56, 89, 0, 34, 333, 34]
    insertion_sort(testlist)
