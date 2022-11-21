temp = 12582912
bintemp = bin(temp).replace("0b", "").zfill(32)
print(bintemp)
print("0-9 bin--->" + bintemp[0:10])
objectType = int("0b" + bintemp[0:10], 2)
objectIn = int("0b" + bintemp[11:], 2)

print(objectType)
print(objectIn)
