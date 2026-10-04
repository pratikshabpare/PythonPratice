# a=int(input("enter the number"))
# b=int(input("enter the numebr"))
# result=a+b
# print("Result:",result)
# Even or odd
# a=7 
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")
#  check number is : positive,Negative,Zero
# a= -5
# if a > 0:
#     print("Positive")
# elif a < 0:
#     print("Negative")
# else:
#     print("Zero")
# Largest among three numbers
# a=25
# b=40
# c=15
# if a < b and a < c:
#     print("smallest =",a)
# elif b < a and b < c:
#     print("smallest =",b)
# else:
#     print("smallest =",c)
# Sum of number from1 to N
# a = 5
# sum=0
# for i in range(1, a + 1):
#     sum=sum + i
# print("Sum =",sum)
# Multiplication table
# a=5 
# for i in range (1,11):
#     print(a * i)
# Factorial of numer
# a = 5
# fact = 1
# for i in  range(1, a + 1) :
#     fact = fact * i
# print(fact) 
# Fibonacci series
# n = 7
# a = 0
# b = 1
# for i in range(n):
#     print(a,end=" ")
#     a,b = b,a+b
# check whether number is prime or not
# n = 17
# is_prime = True
# if n < 2:
#     is_prime = false

# else:
#     for i in range(2,n):
#         if n % i == 0:
#             is_prime = false
#             break
# if is_prime:
#     print("Prime")
# else:
#    print("Not prime")
    #  print all prime numbers from 1 to 50
for n in range(2 ,51):
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
             is_prime= False
             break
    if is_prime:
        print(n,end="")