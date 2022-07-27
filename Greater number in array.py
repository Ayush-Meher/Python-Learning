from array import *
arr = array('i',[23,34,5,6])
for i in range(3):
    if arr[i]>arr[i+1]:
        temp = arr[i]
        arr[i]=arr[i+1]
        arr[i+1]=temp
print(arr[3])