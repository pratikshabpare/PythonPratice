# a=[25,10,40,15,30]
# small=a[0]
# secondsmall=a[0]
# thir
# for i in a:
#     if i < small:
#         secondsmall=small
#         small=i
#     elif i < secondsmall and i != small:
#         secondsmall=i
# print("Smallest :",small)
# print("Second Smallest:",secondsmall)

# numbers=[10,25,8,40,15,30]
# largest=0
# second_largest=0
# third_largest=0
# for num in numbers:
#     if num > largest:
#         third_largest=second_largest
#         second_largest=largest
#         largest=num
#     elif num > second_largest and num != largest:
#         third_largest=second_largest
#         second_largest=num
#     elif num > third_largest and num != second_largest and num != largest:
#         third_largest=num
# print("Third largest:",third_largest)

# numbers=[10,20,10,30,20,10]
# frequency={}
# for num in numbers:
#     if num in frequency:
#         frequency[num]+=1
#     else:
#         frequency[num]=1
# print(frequency) 
# first repeated element in a list
# a=[10,20,30,20,40]
# seen=set()
# for num in a:
#     if num in seen:
#         print("First repeated element:",num)
#         break
#     else:
#         seen.add(num)
# list1=[10,20,30,40]
# list2=[20,30,50,60]
# common=[]
# for num in list1:
#     if num in list2:
#         common.append(num)
# print("Common elements:",common)
# numbers=[0,1,0,3,13]
# result=[]
# for i in numbers:
#     if i != 0:
#         result.append(i)
# for i in numbers:
#     if i == 0:
#         result.append(i)
# print(result)
# 
a=[10,20,10,30,20,40]
duplicates=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            if a[i] not in duplicates:
                duplicates.append(a[i])
print("Duplicate elements:",duplicates)