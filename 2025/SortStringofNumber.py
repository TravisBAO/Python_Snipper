# How you would sort a string of numbers as integers after removing duplicates, 
# and returning back the output, as a string

import time


string_under_test = "4378525907"
# expected output is 02345789

def sort_numbers_in_string():

    sorted_numbers = []
    expected_output = ''

    # convert string to list and remove duplicate elements
    for m in range(len(string_under_test)):
        if string_under_test[m] not in sorted_numbers:
            sorted_numbers.append(string_under_test[m])

    # sort the integers in list
    for i in range(len(sorted_numbers) - 1):
        for j in range(i+1, len(sorted_numbers)):
            if sorted_numbers[i] > sorted_numbers[j]:
                sorted_numbers[i], sorted_numbers[j] = sorted_numbers[j], sorted_numbers[i]
            else:
                pass
    
    # join elements together            
    # for i in range(len(sorted_numbers)):
    #     expected_output += sorted_numbers[i]

    # better way to join list. join() should be called once on all elements, not in a loop
    expected_output = ''.join(sorted_numbers)

    print(expected_output)
    

start_time = time.time()
sort_numbers_in_string()
print("--- %s seconds ---" % (time.time() - start_time))
