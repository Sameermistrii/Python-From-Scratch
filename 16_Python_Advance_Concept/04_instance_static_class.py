class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    # Instance method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # Static Method    
    @staticmethod
    def sum(a, b):
        return a+b
    
    # Class Methods 
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company



e1 = Employee("Jack", 3455)
e2 = Employee("Jill", 34355)
# print(Employee.company)
# print(Employee.name) # this will throw an error
# e1.print_info()
# e2.print_info()

# print(e2.sum(5, 23))
print(Employee.company)
e1.change_company("Acer")
print(Employee.company)