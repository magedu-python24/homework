def add(x,y):
    return int(x+y)
def subtract(x,y):
    return int(x-y)
def multiply(x,y):
    return int(x*y)
def divide(x,y):
    return int(x/y)

while True:
    x = int(input("First Number>>>:"))
    y = int(input("Second Number>>>:"))
    cs = input("Input the calculation signs + - * / >>>")
    if cs == "+":
        print(x,"+",y,"=",add(x,y))
    elif cs == "-":
        print(x,"-",y,"=",subtract(x,y))
    elif cs == "*":
        print(x, "*", y, "=", multiply(x, y))
    elif cs == "/":
        print(x,"/",y,"=",divide(x,y))
    else:
        print("The caculation signs is not correct! ")