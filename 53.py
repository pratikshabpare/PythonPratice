# numbers=[10,20,30,40,50]
# sum=0
# for i in numbers:
#     sum = i+sum
# print(sum)
# smallest no 
# numbers=[25,10,45,5,30]
# print(min(numbers))
# count the vowels in the strrnig
# text="programming"
# count=0
# for ch in text:
#     if ch in "aeiou":
#         count +=1
# print("Vowels =",count)
# Count the frquency of each character in a string
text="hello"
frequency = {}
for i in text:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency [i] =1
for ch ,count in frequency.items():
    print(ch,"=",count)