# numbers = [1, 2, 3, 4, 5]

# k = 2

# result = numbers[-k:] + numbers[:-k]

# print(result)
# find the most frequent element
numbers =(10,20,10,30,20,10,40)
frequency={}
for num in numbers:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num] =1
most_frequent=None
highest_count=0
for num, count in frequency.items():
    if count > highest_count:
        highest_count = count
        most_frequent=num 
print(most_frequent)