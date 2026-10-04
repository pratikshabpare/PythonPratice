a=[10,20,10,30,20,40]
duplicates=[]
for i  in a:
    if i not in duplicates:
        duplicates.append(i)
    print(duplicates)