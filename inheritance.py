# OOP
# Single, multiple, and multilevel inheritance in Python

class company():

    def __init__(self, com_name):
        self.com_name = com_name

    def company_info(self):
        print(f"Company Name is {self.com_name}")

    def showme(self):
        print("I am grandfather")


# class country():
#     def __init__(self, country_name):
#         self.country_name = country_name

#     def country_info(self):
#         print(f"Country Name is {self.country_name}")

class department(company):
    def __init__(self, dept_name, com_name):
        self.dept_name = dept_name
        company.__init__(self, com_name)

    def department_info(self):
        print(f"The department info is {self.dept_name} of {self.com_name}")

    def showme(self):
        print("I am father")


class employee(department):
    # def __init__(self, emp_name, com_name, dept_name):
    #     self.emp_name = emp_name
    #     company.__init__(self, com_name)
    #     country.__init__(self, country_name)
    #     # self.com_name = com_name

    # def emp_info(self):
    #     print(f"Employee Name is {self.emp_name}")

    # def all_info_child(self):
    #     print("This is running from employee")
    #     company.company_info(self)
    #     country.country_info(self)
    #     # super().company_info()  # This is the alternative to the above line

    # def full_info(self):
    #     print(
    #         f"Employee Name is {self.emp_name}, Company Name is {self.com_name}, Country Name is {self.country_name}")

    def __init__(self, emp_name, dept_name, com_name):
        self.emp_name = emp_name
        department.__init__(self, dept_name, com_name)

    def all_info(self):
        print(
            f"The department info is {self.dept_name} of {self.com_name}. Employee name is {self.emp_name}")

    # def showme(self):
    #     print("I am child")


emp1 = employee("Nghia", "HR", "ABC")
emp1.showme()
