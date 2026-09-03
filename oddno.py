numbers=[10,15,20,7,8,11]
odd=0
for i in numbers:
    if i %2 !=0:
        odd=odd+1
        print(i)
print("Total odd numbers",odd)