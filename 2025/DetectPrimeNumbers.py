# How you would write a code to detect prime numbers

def detect_prime_numbers(target_number):

    if target_number <= 1:
        print(str(target_number) + " is NOT a prime")
        return
    
    for divided_num in range(2, target_number):
        if (target_number % divided_num != 0):
            continue
        else:
            print(str(target_number) + " is NOT a prime")
            break
    else:
        print(str(target_number) + " is a prime")


detect_prime_numbers(103)


