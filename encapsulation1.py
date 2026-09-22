# class Student:
#     def __init__(self):
#         self.__marks=0
#     def set_marks(self,marks):
#         if 0 <= marks <=100:
#             self.__marks=marks
#         else:
#             print("Invalid marks")
#     def get_marks(self):
#         return self.__marks
# student=Student()
# student.set_marks(85)
# print(student.get_marks())
class Student:
    college_name="DIMR"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_college(cls,new_college):
        cls.college_name=new_college
    def display(self):
        print("Name:",self.name)
        print("College:",self.college_name)
student1=Student("Rahul")
student2=Student("Priya")
print("Before changing college:")
student1.display()
student2.display()
Student.change_college("SPPU")
print("\n After changing college:")
student1.display()
student2.display()