a=12345
total=0
while a>0:
    digit=a%10
    total=total+digit
    a=a//10
print(total)