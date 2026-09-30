try:
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))
    result=num1/num2
    print("Result:",result)
except ZeroDivisionError:
    print("cannot divide by zero")
# Write a Python program that asks the user to enter an integer.

# If the user enters a valid integer, print the number.
# If the user enters something like "abc", handle the ValueError.
# Print "Invalid input. Please enter an integer."
try:
    number=int(input("Enter a number:"))
    print("You entered:",number)
except ValueError:
    print("Invalid input")
numbers=[10,20,30,40,50]
try:
    index=int(input("Enter index:"))
    print("Element:",numbers[index])
except IndexError:
    print("Invalid index. Index is out of range")
except ValueError:
    print("Please enter a valis integer index")   
student={
    "name":"Pratiksha",
    "age":23,
    "city":"Pune"
}
try:
    print(student["salary"])
except KeyError:
    print("Key does not exist")