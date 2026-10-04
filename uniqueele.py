# list1=[10,20,30,40]
# list2=[30,40,50,60]
# unique=[]
# for i in list1:
#     if i not in list2:
#         unique.append(i)
# for i in list2:
#     if i not in list1:
#         unique.append(i)
# print(unique)
# how  many elements in a list are greater than a given number,without using count() or any bulit methods
numbers=[10,25,40,15,60,30]
target=25
count=0
for i in numbers:
    if i > target:
        count += 1
print(count)
