import sys
print(sys.path)

map = {
"{":"}",
"[":"]",
"(":")"
}

s = "()[]{}"
for x in s:
    if x in map:
        print("The Key " + str(x) + " is mapped to " + map[x] + " in dictionary")
        print("\n")
    else:
        print(str(x) + " is not included in keys of dictionary")
        print("\n")