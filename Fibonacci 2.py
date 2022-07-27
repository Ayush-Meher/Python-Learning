a=0
b=1
x=int(input("Enter the number"))
y=2
print(a)
print(b)
while y < x:
    
    
    c=a+b
    a=b
    b=c
    y+=1
    print(c)
    if c<=x:
        pass
    else:
        break
    
    