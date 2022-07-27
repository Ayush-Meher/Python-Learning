def fact(n):
    y=1
    for i in range(1,n+1):
        y= y*i
    print(y)
x= int(input("ENter the number"))
fact(x)