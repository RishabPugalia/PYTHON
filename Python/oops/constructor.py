class employee:
    def __init__(self, salary, name, bond):
        self.salary = salary # create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
     

    def get_salary(self): # self is a way to reference the object of the class which is created
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")

e1 = employee(34000, "John Doe", 4)
# print(e1.get_salary())
e1.get_info()