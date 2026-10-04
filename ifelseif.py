print("enter your age:")
Age=int(input())
if(Age <= 5):
    print("Free entry")
elif(Age > 5 and Age <= 18):
    print("Ticket price : 900")
elif(Age > 18 and Age <=40):
    print("Ticket price is : 1200")
else:
    print("Tickt price is 500")