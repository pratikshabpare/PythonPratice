# num=17
# if num <=1:
#     print("Not a prime number")
# else:
#     prime=True
#     for i in range(2,num):
#         if num % i==0:
#             prime=False
#             break
# if prime:
#     print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")
num=5
fact=1
for i in range(1,num+1):
    fact=fact * i
print("Factoril =",fact)
    