import os
import sys
print(" SYSTEM INFORMATION ")

print("os Name : ",os.name)
print("Current Folder :",os.getcwd())
print("Platform :",sys.platform)

for file in os.listdir():
    print(file)