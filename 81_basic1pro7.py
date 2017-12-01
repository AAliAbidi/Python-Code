#Printing file extension
filename = input("Enter file name: ")
file_Extn = filename.split(".")
print("Extension is" +repr(file_Extn[-1]) )
