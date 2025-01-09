# How you would use an algorithm to find a number between 1-100
MINIMUM = 1
MAXIMUM = 100

def find_Number_between_1_and_100(input_value):
    temp_min = MINIMUM
    temp_max = MAXIMUM
    target_number = 0
    find_loop = 10
    while find_loop > 1:
        print(temp_min)
        print(temp_max)
        print(">>>>>>>>>>>>>>>>>")
        temp_middle = (temp_min + temp_max) // 2
        if input_value > temp_middle:
            temp_min = temp_middle + 1
            find_loop -= 1
        elif input_value < temp_middle:
            temp_max = temp_middle - 1
            find_loop -= 1
        else:
            target_number = input_value
            find_loop -= 1
            break
    print (target_number)


find_Number_between_1_and_100(100)