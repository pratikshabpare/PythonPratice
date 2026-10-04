numbers=[10,45,23,89,12,67]
largest=numbers[0]
second=numbers[0]
for num in numbers:
    if num > largest:
        second=largest
        largest=num
    elif num > second:
        second=num
print("Second Largest =",second)