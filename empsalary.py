#Create an employee salary program where the salary can be viewed and modified only through
# appropriate methods
class employee:
    def __init__(self,salary):
        self.salary=salary


    def increase_salary(self,percentage):
        self.salary += percentage

    def decrease_salary(self,percentage):
            self.salary -= percentage

    def display_salary(self):
        print("updated salary:",self.salary)


salary=int(input("Enter your salary:"))


p= employee(salary)
print("1.Add Salary")
print("2.Decrease Salary")
choice=int(input("enter the choice:"))
if choice ==1:
     percentage=float(input("enter the salary to add:"))
     p.increase_salary(percentage)
else:
     percentage=float(input("enter the salary to decrease:"))
     p.decrease_salary(percentage)
p.display_salary()