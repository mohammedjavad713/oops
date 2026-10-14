class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("*******************")
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
salary = float(input("Enter employee salary: "))

emp = Employee(name, emp_id, salary)

emp. display()
