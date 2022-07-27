from array import *
a = array("i", [])
n = int(input("Enter the length of array\n"))
for i in range(n):
    m = int(input("Enter the number\n"))
    a.append(m)
j = int(input("Enter the index number you want to remove\n"))
k = 0
for e in range(j+1):
    a.