


def sort(seq):
    for i in range(len(seq)-1,0,-1):
        for j in range(i):
            if seq[j]>seq[j+1]:
                temp=seq[j]
                seq[j]=seq[j+1]
                seq[j+1]=temp
                


list=[4,6,2,3,9,7,8]

sort(list)
print(list)