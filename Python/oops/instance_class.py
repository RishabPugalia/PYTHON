class employee:
    company = "Asus" # class attribute

    def __init__(self, salary, name, bond, company):
        self.salary = salary # create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company
     

    def get_salary(self): # self is a way to reference the object of the class which is created
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")

e1 = employee(34000, "John Doe", 4, "Tesla")
print(e1.company) # will always print instance attribute whenever present
print(employee.company) # this always print the class attribute

#object introspection

print(dir(e1))