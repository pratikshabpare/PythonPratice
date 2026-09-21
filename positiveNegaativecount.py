numbers=[10,-5,20,-8,0,15,-2]
positive=0
negative=0
for i in numbers:
    if i > 0: 
        positive=positive+1
    elif i< 0:
        negative=negative+1
print("Total positive numbers:", positive)
print("Total negative numbers:", negative)