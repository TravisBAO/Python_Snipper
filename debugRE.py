import os
import re

logline = "----------Malloc Size: 144, 0x60342810"
firsthalf = "----------Malloc Size: "

logNumber = re.search(firsthalf + "(.*)" + ", 0x", logline).group(1)
print(logNumber)