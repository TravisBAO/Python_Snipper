# Write a function which receives a string contains only alphabetic characters as parameter, if the length of the maximum consecutive repeating character is greater than half of the whole string length, return the character in lowercase, otherwise, return "Null". Consider the lowercase and uppercase character is the same, for example, "aA" is consecutive repeating.

#aabbbcc => Null
#ccddaaaaa => a



stringUnderTest = "aabbbbbbcc"
stringUnderTest = stringUnderTest.lower()
stringLength = len(stringUnderTest)

MaxRepeatNum = 1
repeatCharList = [stringUnderTest[0]]
repeatTimeList = []

for i in range(1, stringLength):
    if stringUnderTest[i] == stringUnderTest[i - 1]:
        MaxRepeatNum += 1
    else:
        repeatCharList.append(stringUnderTest[i])
        repeatTimeList.append(MaxRepeatNum)
        MaxRepeatNum = 1

    if i == stringLength - 1:
        repeatTimeList.append(MaxRepeatNum + 1)

MaxRepeatNum = max(repeatTimeList)
indexOfMaxRepeat = repeatTimeList.index(MaxRepeatNum)

if MaxRepeatNum > int(stringLength / 2):
    result = repeatCharList[indexOfMaxRepeat]
else:
    result = "Null"

print(result)
