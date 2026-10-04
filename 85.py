numbers=[10,20,10,30,20,10,40]
frequency={}
for num in numbers:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
most_frequent=max(frequency,key=frequency.get)
print(most_frequent)