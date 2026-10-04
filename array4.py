# import array as arr
# numbers=arr.array("i",[1,2,3,3,4])
# del numbers[2]
# print(numbers)
# from array import *
# numbers=array("i",[10,20,30,40,50])
# length=len(numbers)
# print(length)
# Array concatenation
import array as arr

a=arr.array("d",[1.1,2.1,3.1,2.6,7.8])
b=arr.array('d',[3.7,8.6])
c=arr.array('d')
c=a+b
print("Array c =",c)