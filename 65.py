# data={
#     "Java":85,
#     "Python":92,
#     "SQL":88,
#     "Angular":78
# }
# highest_key=max(data,key=data.get)
# print(highest_key)
# Merge two dictionaries
# dict1={"a":10,"b":20}
# dict2={"c":30,"d":40}
# dict1.update(dict2)
# print(dict1)
# non-repeating character

# text="aabbcde"
# for char in text:
#     if text.count(char)==1:
#         print(char)
#         break
# removee duplicate from list without using set()
# numbers=[10,20,10,30,20,40,30]
# unique=[]
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print(unique)
# numbers=[10,45,20,80,60,35]
# largest=numbers[0]
# second_largest=numbers[0]
# for num in numbers:
#     if num > largest:
#         second_largest=largest
#         largest=num
#     elif num > second_largest and num != largest:
#         second_largest=num
# print(second_largest)
# count the vowels and consonants
# text="Python Programming"
# vowels=0
# consonants=0
# for char in text.lower():
#     if char in "aeiou":
#         vowels +=1
#     elif char.isalpha():
#         consonants +=1
# print("Vowels =",vowels)
# print("Consonants =",consonants)

# first duplicate
# numbers=[10,20,30,20,40,30]
# seen=[]
# for num in numbers:
#     if num in seen:
#         print(num)
#         break
#     else:
#         seen.append(num)
# find all duplicate elements in list
numbers=[10,20,30,20,40,30,50,10]
seen=[]
duplicates=[]
for num in numbers:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.append(num)
print(duplicates)
