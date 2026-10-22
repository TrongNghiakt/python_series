class employee():

    company_name = "ABC Corporation"

    def __init__(self, emp_name, emp_dept):
        self.emp_name = emp_name
        self.emp_dept = emp_dept

    @classmethod
    def changes(cls, new_company):
        cls.company_name = new_company

    # Alternative to Class method
    # def changesInClass(self, new_company):
    #     employee.company_name = new_company

    # Instance method
    @property  # Getter
    def info(self):
        print(
            f"Employee {self.emp_name} works in {self.emp_dept} department at {self.company_name}.")

    @info.setter
    def info(self, new_empdetails):
        new_emp_name = new_empdetails[0]
        new_emp_dept = new_empdetails[1]

        self.emp_name = new_emp_name
        self.emp_dept = new_emp_dept

    @staticmethod
    def addition(x, y):
        return x + y

    # Setter
    def changeinfo(self, new_name, new_dept):
        self.emp_name = new_name
        self.emp_dept = new_dept


emp1 = employee("John Doe", "Sales")
emp2 = employee("Jane Smith", "Marketing")

# print(emp1.addition(5, 10))
# emp1.changesInClass("NewNewCompany")
# print(emp1.company_name)  # Output: NewNewCompany

# emp1.changes("XYZ Corporation")
# # Output: Employee John Doe works in Sales department at XYZ Corporation.
# emp1.info()


# emp1.info()
# emp1.changeinfo("John Smith", "Finance")
# emp1.info()

emp1.info = ["John Smith", "Finance"]
print(emp1.info)
