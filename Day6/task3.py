class Employee:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = f"{firstname} {lastname}"
        self.email = f"{firstname}.{lastname}@company.com"

emp_1 =Employee("Raj", "Raiyani")
emp_2 = Employee("meet", "vekariya")
emp_3 = Employee("jay", "thumar")

print(emp_1.fullname)
print(emp_2.email)
print(emp_3.firstname)