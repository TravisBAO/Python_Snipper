import os
import sys

number_string = "0123456789"

print("2 to 6: " + number_string[2:6])
print("\n")
print("2 to end: " + number_string[2:])
print("total string: " + number_string[:])
print("\n")
print("index -1: " + number_string[-1])
print("从index=2开始, 到倒数第二个: " + number_string[2:-2])
print("\n")
print("从头开始, 二选一: " + number_string[::2])
print("从index=1开始, 二选一: " + number_string[1::2])


cPath = os.getcwd()

DPath = os.getcwd().split("ContinuousIntegration")
print(DPath)


FPath = os.getcwd().split("ContinuousIntegration")[0] + "ContinuousIntegration" + "\\xxxxxxx"
print("FPath= " + FPath)