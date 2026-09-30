# a=20
# if a > 20:
#     print("Greater than 20")
# elif a ==  20:
#     print("Equal to 20")
# else:
#     print("Less than 20")
# shopping_bag=['apples','bread','eggs','milk','coffee beans','tomatoes']
# print("Given list:",shopping_bag)
# print("\n Iterating Over List using 'for' Loop:")
# for item in shopping_bag:
#     print(item)
# print("\n Iterating Over List using'while'Loop:")
# index=0
# while index < len(shopping_bag):
#     print(shopping_bag[index])
#     index +=1
# break ,continue,pass
# for i in range(20):
#     if i == 14:
#         break
#     if i % 2 == 0:
#         continue
#     if i == 9:
#         pass 
#     print(i)
# use of def keyyword
# def greeting():
#     print("Welcome to tpoint Tech!")
# greeting()
# return and yeild keyword
# def add_numbers(num1,num2):
#     return num1+num2
# def generate_number(num1):
#     for i in range(num1):
#         yield i
# print("Addition of 12 and 5 is ",add_numbers(12,5))
# for i in generate_number(5):
#     print("Generated Number:",i)
# lambda keyword
# square_of_num=lambda num : num * num
# print("Square of 12 is",square_of_num(12))
# global keyword
# p=12
# def func_one():
#     global p 
#     p = 19
# func_one()
# print(p)
nested_lst=[[14,6,8],[13,18,25],[72,48,69]]
print("Nested List:",nested_lst)
print("\n Accessing elements of Nested List:")
print("nested_lst[0]:",nested_lst[0])
print("nested_lst[0][1]:",nested_lst[0][1])
print("\n Iterating through Nested list using 'for' loop:")
for sublist in nested_lst:
    for item in sublist:
        print(item)
print("\n Adding element to Nested list:")
nested_lst[0].append(10)
print("New Nested List:",nested_lst)