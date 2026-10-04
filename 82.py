# fruits={
#     'apple':20,
#     'banana':14,
#     'watermelon':2,
#     'kiwi':12,
#     'oranges':24
    
# }
# print("Given Dictionary:",fruits)
# popped_value=fruits.pop('kiwi')
# print("Popped Value:",popped_value)
# print("Updated Dictionary:",fruits)
# car_details={
#     "brand":"Tata",
#     "model":"Sierra",
#     "year":2025
# }
# a=car_details.get("model")
# print(a)
# first_dictionary={'A':'Tpoint Tech','B':'Python'}
# second_dictionary={'B':}
# def welcome(name):
#     print(f"Hello{name}! welcome to Tpoint Tech")
# welcome("John")
# def greet(*names):
#    """this function greets multiple user"""
#    for name in names:
#        print(f"Hello,{name} ! welcome to python programming")
# greet("Alice","Bob","Charlie")
    
# def add(a,b):
#     return a+b
# result=add(3,5)
# print(f"The sum is{result}")
# def factorial(n):
#     if n == 1:
#         return 1 
#     else:
#         return n * factorial(n-1)
# result=factorial(5)
# print(f"The factorial of 5 is {result}")
# result=dict()
# result2=dict(a=1,b=2)
# print(result)
# print(result2)
# fliter function 
# def filterdata(x):
#     if x > 5:
#         return x 
# result=filter(filterdata,(1,2,6))
# print(list(result))
# n = lambda x: x + 10
# print(n(10))
# lambda function with multiple arugments
# n=lambda x,y:x * y 
# print(n(2,10))
# n=lambda x:"zero" if x== 0 else "Even" if x % 2 == 0 else "odd"
# print(n(5))
# n=[lambda a=x: a * 10 for x in range(1,6)]
# for i in n:
#     print(i())
class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.salary=salary
    def show_details(self):
        print("Name:",self.name)
        print("Role:",self.role)
        print("Salary:",self.salary)
emp1=Employee("Rahul","Software Developer",6000)
emp1.show_details()