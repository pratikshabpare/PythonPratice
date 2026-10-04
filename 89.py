# python program to show how __init__ method works
class methods():
    def __init__(self,*args):
        print("Now called __init__ magic method after the initialised parameters")
        self.name=args[0]
        self.std=args[1]
        self.marks=args[2]
Student = methods("Itik",11,98)
print(Student)
print(f"Name,standard,and marks of the student is:\n",Student.name,"\n",Student.std,"\n",Student.marks)