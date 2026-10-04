a=[10,20,30,20,40,10,30]
duplicates=[]
for i in a:
    if a.count(i)>1 and i not in duplicates:
        duplicates.append(i)
print(duplicates)