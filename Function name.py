lst = []
x = int(input("How many names do you have?\n"))
o=1
while o<=x:
    names = input("Enter the name\n")
    lst.append(names)
    o+=1
y= int(input("Enter the number of letters\n"))
j=0
def name(z):
    for i in lst:
        if len(i)>z:
            global j
            j+=1

name (y)

     

print(j, "no. of people have more than", y , "lettered names")
            
