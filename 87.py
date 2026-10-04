# numbers=[10,20,30,20,40,10]
# seen=set()
# for num in numbers:
#     if num in seen:
#         print(num)
#         break
#     seen.add(num)
list1=[10,20,30,40,50]
list2=[30,40,60,70,50]
result=[]
for i in list1:
    if i in list2:
        result.append(i)
print(result)