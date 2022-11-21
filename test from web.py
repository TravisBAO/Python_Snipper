a = [1, 2, 3, 4, 5]
b = []
x = 0
# 这里很tricky， a[x] = a[0] = 1 不会跟着一直增一
for x in range(a[x]):
    print("current x is " + str(x))
    b.append(a[x])
print(b) # output: [1]
