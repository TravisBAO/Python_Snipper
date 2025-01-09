def  triangles(max):
    row = [1]
    n = 0
    while (n < max):
        n = n + 1
        yield row
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

yanghui = triangles(6)
for x in yanghui:
    print(x)