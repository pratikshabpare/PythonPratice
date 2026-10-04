# def check_age(age):
#     if age < 18:
#         raise Exception("Age must be 18 or above")
#     else:
#         print("Age is valid")
# try:
#     check_age(17)
# except Exception as e:
#     print("An error Occurred:",e)
    
# try:
#     value=int("a")
# except ValueError:
#     print("Invalid value")
# except TypeError:
#     print("IInvalid type")

try:
    result=10/0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("The finally block is always exectued")  