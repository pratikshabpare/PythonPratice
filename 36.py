a=[10,20,30,40]
b=[20,40,50,60]
c=[]
for i in a:
    for j in b:
        if i==j:
            c.append(i)
            print(c)