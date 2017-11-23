from sys import argv
script, filename = argv
txt = open(filename)
print("Here's the file %r:" %filename)
print (txt.read())
txt.close()
print ("Type the file name again %r" %filename)
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())
txt_again.close()
