a=[10,15,20,25,30]
even=0
odd=0
for i in a:
    if i % 2 ==0:
        even=even+1
    else:
        odd=odd+1
print("even:",even)
print("odd:",odd)