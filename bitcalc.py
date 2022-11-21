
inalarm = False
faultValue = True
overriddernValue = True
osvalue = True
if inalarm: int1 = 8 
else: int1 =0
if faultValue: int2 = 4
if overriddernValue: int3 =2
if osvalue: int4 =1
tempvalue = int1 + int2 + int3 +int4
propvalue = bin(tempvalue)
propvalue = propvalue.replace("0b", "")
print(propvalue)


