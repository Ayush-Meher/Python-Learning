i=["A","B","C","D"]
j=["A","P","Q","R"]
for l in range(0,4,1):
    j.pop(l)
    j.insert(l, i[l])
    print(j)
