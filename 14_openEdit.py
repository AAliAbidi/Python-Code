from sys import argv
scripr, filename = argv

print("We are going to erase %r." %filename)
print("If you don't want that, hit CTRL+C (^c)")
print("If you do want that, hit RETURN")

input("?")

print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm asking you 3 lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally going to close that file")
target.close()

