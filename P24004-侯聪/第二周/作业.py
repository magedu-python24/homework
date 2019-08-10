while True:
    x = int(input("Input the First Number>>>"))
    cs = input ("Input the Calculating signs + = * / >>>")
    list = ['+','-','*','/']
    if cs not in list:
        print("The Calculation signs U input is not Correct!!!!")
        continue
    y = int(input("Input the Second Number>>>"))

    if cs == "+":
        print(x,"+",y,"=",x+y)
    elif cs == "-":
        print(x,"-",y,"=",x-y)
    elif cs == "*":
        print(x,"*",y,"=",x*y)
    else :
        print(x,"/",y,"=",x/y)
