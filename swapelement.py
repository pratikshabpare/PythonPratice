# numbers=[10,20,30,40,50]
# numbers[0],numbers[len(numbers)-1]=numbers[len(numbers)-1],numbers[0]
# print(numbers)
# numbers=[10,20,30,40,50]
# reverse=[]
# for i in range(len(numbers) -1,-1,-1):
#     reverse.append(numbers[i])
# print(reverse)
# numbers=[20,10,30,10,40,20,5]
# small=float(''inf)
# secondsmall=0
# for i in numbers:
#     if i < numbers:
#         secondsmall=small
#         small=i
#     elif i < secondsmall and i != small:
#         secondsmall =i 
# print("Smallest:",small)
# print("second smallest",secondsmall)
# common elements between two lists
list1=[10,20,30,40,50]
list2=[30,40,50,60,70]
common=[]

for i in list1:
    if i in list2 and i not in common:
        common.append(i)
print(common)