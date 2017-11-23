from sys import argv
from os.path import exists
script, filename = argv
print("***************************************************************")
print("* Note                                                        *")
print("*------                                                       *")
print("*1. Does File Already Exist %s                              *" %exists(filename)            )
print("*2. To exit press CTRL+C                                      *")
print("*3. Press RETURN to continu                                   *")
print("*                                                             *")
print("***************************************************************")

fileopen = open(filename, 'w')
#size = fileopen.read()
print("FILE INFO BEFORE EDITING")
print("----------------------------")
print("1. File name = %s\n2" %(filename))
print("----------------------------\n")
print("WRITE THREE LINE TO FILE")
fileopen.truncate()
line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

fileopen.write(line1)
fileopen.write("\n")
fileopen.write(line2)
fileopen.write("\n")
fileopen.write(line3)
fileopen.write("")
#fileopen.close()

print("Now reading a file")
print("------------------")
fileopen = open(filename)
size = fileopen.read()
print("FILE AFTER EDITING")
print("--------------------")
print("1. File name = %s\n2. File size = %d bytes\n3. File content \n-----------------------\n %s\n " %(filename, len(size), size))







