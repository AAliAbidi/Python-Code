def intake(var):
    newstr = " "
    print ("String is :", var)
    pun = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in var:
        if char not in pun:
            newstr+=char

    print(newstr)


intake("Let's try, Mike.")
