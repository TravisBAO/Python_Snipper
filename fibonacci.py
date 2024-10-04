

def generate_fibonacci(list_length):
    fibonacci = []
    if list_length == 1:
        fibonacci.append(1)
    elif list_length == 2:
        fibonacci = [1,1]
    else:
        fibonacci = [1,1]
        for i in range (2, list_length):
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    print(fibonacci)

if __name__ == "__main__":
    generate_fibonacci(12)