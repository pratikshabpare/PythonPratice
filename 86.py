# dict1 = {"a": 10, "b": 20}
# dict2 = {"c": 30, "d": 40}

# c = dict1.copy()
# c.update(dict2)

# print(c)
numbere=[10,25,40,25,30,40,15]
result=set(numbere)
print(result)
largest=0
second_largest=0
for i in result:
    if i > largest:
        second_largest=largest
        largest=i
    elif i > second_largest:
        second_largest= i
print("Largest:",largest)
print("second largest:",second_largest) 