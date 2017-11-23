from sys import argv
script, filename = argv
openfile = open(filename)
size = openfile.read()
print("File Name = %s \nFile Size = %d byte long\nFile Content is:\n%s"%(filename, len(size), size))
