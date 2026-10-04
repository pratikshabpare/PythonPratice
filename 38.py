a=[10,20,10,30,20,10]
for i in a:
    count=0
    for j in a:
        if i==j:
            count=count+1
    print(i,"=",count)