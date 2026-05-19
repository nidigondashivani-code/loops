l=[1,1,4,5,6]
l2=[1,4,7,8,9]
k=[]
for i in l:
    for j in l2:
        if j not in k and i==j:
            k.append(j)
          
print(k)