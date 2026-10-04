a=[10,25,7,40,15]
largest=[0]
secondLargest=[0]
for i in a:
    if i > largest:
        secondLargest=largest
        largest=i
    elif i> secondLargest and i != largest:
        secondLargest=i
print(secondLargest)
print("LArgest:",largest)