a = 18
b = 30
c = 20

if a > b:
    if b > c:
        sumOf = a + b
    else:  # c > b
        sumOf = a + c
else:  # b > a
    if a > c:
        sumOf = a + b
    else:  # c > a
        sumOf = b + c

print(sumOf)
