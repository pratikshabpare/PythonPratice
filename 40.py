a=[10,20,20,30,40]
b=[20,20,40,50]
intersection=[]
for i in a:
    if i in b and i not in intersection:
        intersection.append(i)
print(intersection)