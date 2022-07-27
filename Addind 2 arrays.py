from array import *
a = array("i",[1,2,3,4])
b = array("i",[5,6,7,8])
c = array("i",[])
k=0
for i in a:
    l= i + (b[k])
    k+=1
    c.append(l)
print(c)