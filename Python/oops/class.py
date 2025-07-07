class employee:
    company = "HP"

    def get_salary(self): # self is a way to reference the object of the class which is created
        return 34000


e = employee() # an object of class employee is created here
print(e.get_salary()) # e's get salary method is called
print(e.company)
e2 = employee()
print(e2.get_salary())
print(e2.company)