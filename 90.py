# class Method:
#     def __init__(self,a):
#         self.a=a
#     def __call__(self,number):
#         return self.a * number
# instance=Method(7)
# print(instance.a)
# print(instance(5))
# a=["Python","C","Android"]
# a.push("Java")
# a.pop("C++")
# print(a)
# print(a.pop())
# print(a)
# numlist=[4,32,6,76,12,37,52]
# square=[sol ** 2 for sol in numlist]
# print(square)
from collections import Counter
data=['a','b','a','c','b','a']
count=Counter(data)
print(count)