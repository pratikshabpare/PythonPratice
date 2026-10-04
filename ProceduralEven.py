# def CheckEven(No):
#     if(No % 2 == 0):
#         print("Its Even numbers")
#     else:
#         print("Its off")
# def main():
#     Value=int(input("Enter Number:"))
#     CheckEven(Value)
# if __name__=="__main__":
#     main()
# def CheckEven(No):
#     if(No % 2 == 0):
#         return True
#     else:
#         return False
# def main():
#     Value=int(input("Enter Number:"))
#     Ret=CheckEven(Value)
#     if(Ret == True):
#         print("Its Even Number")
#     else:
#         print("Its off Number")
# if __name__=="__main__":
#     main()
def CheckEven(No):
    return (No % 2 == 0)
def main():
    Value=int(input("Enter Number"))
    Ret=CheckEven(Value)
    if(Ret == True):
        print("Its Even Number")
    else:
        print("Its Odd Number")
if __name__=="__main__":
    main()