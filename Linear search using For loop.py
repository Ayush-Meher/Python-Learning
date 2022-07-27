pos = 0

def search(seq,a):
    j=1
    for i in seq:
        if i == a:
            globals()["pos"]=j
            return True
        j+=1
    return False
        
    

        



a = [8,2,5,1,6,3,9]

x= int(input("Enter the number you want to search\n"))

if search(a,3):
    print("Found at",pos)

else:
    print("Not fonud")





