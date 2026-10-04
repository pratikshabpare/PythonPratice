class  Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)
employee1=Employee("Rahul",30000,"IT")
employee2=Employee("Priya",40000,"HR")
print("Employee 1:")
employee1.display()
print("\nEmployee 2:")
employee2.display()