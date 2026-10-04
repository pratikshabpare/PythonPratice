a=121
reverse=0
while a>0:
    digit=a % 10
    reverse=reverse * 10 +digit
    a = a //10
print(reverse)
if a==reverse:
    print("the number is palindrome")
else:
    print("the number is not palindrome")