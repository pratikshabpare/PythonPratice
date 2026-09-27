list1=[10,20,30,40]
list2=[30,40,50,60]
list3=[]
for i in list1:
    if i not in list3:
        list3.append(i)
for i in list2:
    if i not in list3:
        list3.append(i)
print(list3)