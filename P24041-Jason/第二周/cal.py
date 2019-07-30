while 1:
    num1=float(input("请输入一个数字："))
    cal=input("请输入运算符：")
    num2=float(input("请输入一个数字："))
    if cal=="+":
        print(num1,cal,num2,"=",num1+num2)
    elif cal=="-":
        print(num1,cal,num2,"=",num1-num2)
    elif cal=="*":
        print(num1,cal,num2,"=",num1*num2)
    elif cal=="/":
        print(num1,cal,num2,"=",num1/num2)
    else:
        print("wrong input!")
    choice=input("是否退出计算器？ Y/N")
    if choice=="Y":
        break
    else:
        print("---------------------------")
        continue
