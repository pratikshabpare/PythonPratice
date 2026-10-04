a=[10,25,7,40,30]
small=0
secondSmall=0
for i in a:
    if i > small:
        secondSmall=small
        small=i
    elif i > secondSmall and i != small:
        secondSmall=i
    print("Largest:",small)
    print("Second Largest:",secondSmall)