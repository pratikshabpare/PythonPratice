# class Employer:
#     def __init__(self,name,industry):
#         self.name=name
#         self.industry=industry
#     def display_info(self):
#         print(f"Employer:{self.name}-{self.industry}")
# employer_one=Employer("Tpoint Tech","Education")
# employer_one.display_info()
class Employer:
    def __init__(self,employee_count):
        self.__employee_count=employee_count
    def get_employee_count(self):
        return self.__employee_count
employer_one=Employer(1500)
print("No.of Employees:",employer_one.get_employee_count())
p