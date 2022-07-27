pos = 0

def search(list,a):
    l=0
    u=len(list)
    
    

    while l <= u:
        
        mid= (l+u)//2
        if list[mid]== a:
            globals()["pos"] = mid
            
            return True
        else:
            if list[mid]<a:
                l = mid
            else:
                u = mid
    return False





a=[2,9,12,23,34,45,56,78,89,90]
n=23

if search(a,n):
    print("Found at", pos +1)
else:
    print("Not Found")