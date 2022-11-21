tempValue = "NULL"
if (tempValue != "NULL") and (tempValue.find('.') == -1):
    propertyValue = tempValue + ".0"
else:
    propertyValue = tempValue

print(str(propertyValue))