for i in range(-3,4):
    if i<0:
        print(" "*abs(i),"*"*(4+i))
    elif i==0:
        print(" "*0,"*"*7)
    else:
        print(" "*3,"*"*(4-i))
