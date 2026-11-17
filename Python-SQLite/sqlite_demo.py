import sqlite3
from employee import Employee

conn = sqlite3.connect(":memory:")  # Create an in-memory database
# conn = sqlite3.connect("employee.db")  # Create a database file
c = conn.cursor()


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {
            "first": emp.first, "last": emp.last, "pay": emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {"last": lastname})
    return c.fetchall()  # Fetch all remaining rows of the result set


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""",
                  {"first": emp.first, "last": emp.last, "pay": pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first = :first AND last = :last", {
                  "first": emp.first, "last": emp.last})


c.execute("""
CREATE TABLE IF NOT EXISTS employees (first text, last text, pay integer)""")

# c.execute("""INSERT INTO employees VALUES ('Marry', 'Doe', 70000)""")

# c.execute("INSERT INTO employees VALUES (?,?,?)",
#           (emp1.first, emp1.last, emp1.pay))

# conn.commit()  # Commit the changes to the database

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {
#           "first": emp2.first, "last": emp2.last, "pay": emp2.pay})

# conn.commit()


# c.execute("SELECT * FROM employees WHERE last=?", ("Doe",))
# print(c.fetchall())  # Fetch all remaining rows of the result set
# # print(c.fetchone())  # Fetch the first row of the result set
# # c.fetchmany(3)  # Fetch the next 3 rows of the result set

# c.execute("SELECT * FROM employees WHERE last=:last", {"last": "Smith"})
# print(c.fetchall())  # Fetch all remaining rows of the result set

conn.commit()  # Commit the changes to the database

emp1 = Employee("John", "Doe", 50000)
emp2 = Employee("Jane", "Doe", 60000)

insert_emp(emp1)
insert_emp(emp2)

emps = get_emps_by_name("Doe")
print(emps)

update_pay(emp2, 95000)
remove_emp(emp1)

emps = get_emps_by_name("Doe")
print(emps)

conn.close()
