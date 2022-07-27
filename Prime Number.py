a=int(input("Enter your number\n"))
b=0
for i in range(1,a,1):
    if a%i==0:
        b+=1
    
if b<=2:
    print("Your Number is Prime")
else:
    print("Your Number is Not Prime")