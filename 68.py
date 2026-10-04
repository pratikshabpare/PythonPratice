# numbers=[25,10,40,5,30,15]
# small=0
# secondSmall=0
# for i in numbers:
#     if i < small:
#         secondSmall=small
#         small=i
#     elif i < secondSmall and i != small:
#         secondSmall=i
# print("Second Smallest element =",secondSmall) 
# list1=[10,20,30,40,50]
# list2=[30,40,60,70,50]
# common=set(list1) & set(list2)
# print("Common elements=",common)
# numbers=(25,10,40,5,30,15)
# maximum=numbers[0]
# minimum=numbers[0]
# for num in numbers:
#     if num > maximum:
#         maximum=num
#     if num < minimum:
#         minimum=num
# print("Maximum =",maximum)
# print("Minimum =",minimum)
# text="Programming"
# frequency={}
# for char in text:
#     if char in frequency:
#         frequency[char] +=1
#     else:
#         frequency[char] = 1
# for char,count in frequency.items():
#     print(char,":",count)
# text="aabbcdeeff"
# frequency={}
# for char in text:
#     if char in frequency:
#         frequency[char] +=1
#     else:
#         frequency[char] = 1
# for char in text:
#     if frequency[char]==1:
#         print("First non-repeating character =", char)
#         break
# numbers=[10,20,30,20,40,10,50,30]
# duplicates=[]
# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)
# print("Duplicate elements =",duplicates)
# numbers=[0,1,0,3,12]
# result=[]
# for num in numbers:
#     if num !=0:
#         result.append(num)
# for num in numbers:
#     if num == 0:
#         result.append(num)
# print(result)
# dict1={"a":10,"b":20,"c":30}
# dict2={"b":5,"c":15,"d":40}
# result=dict1.copy()
# for key,value in dict2.items():
#     if key in result:
#         result[key] += value
#     else:
#         result[key] = value
# print(result)
# text1="listen"
# text2="silent"
# if len(text1) != len(text2):
#     print("Strings are not anagrams")
# else:
#     frequency1={}
#     frequency2={}
#     for char in text1:
#         if char in frequency1:
#             frequency1[char]+=1
#         else:
#             frequency1[char]=1
#     for char in text2:
#         if char in frequency2:
#             frequency2[char]+=1
#         else:
#             frequency2[char]=1
#     if frequency1 == frequency2:
#         print("Strings are anagrams")
#     else:
#         print("Strings are not anagrams")
# class Student:
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Course:",self.course)
# student1=Student("Pratiksha",23,"MCA")
# student1.display()
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if amount <= self.__balance:
            