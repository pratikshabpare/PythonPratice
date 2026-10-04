numbers=[10,-5,20,-8,30,-2]
Positive=[]
Negative=[]
for i in numbers:
    if i > 0:
        Positive.append(i)
    if i < 0:
        Negative.append(i)
print("Positive:",Positive)
print("Negative:",Negative)