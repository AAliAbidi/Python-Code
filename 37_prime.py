for i in range(2,30):
    for b in range(2, i):
        if i%b == 0:
            break
    else:
        print(i)
