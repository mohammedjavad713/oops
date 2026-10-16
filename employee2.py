class employee:
    def __init__(self,salary):
        self.salary=salary


    def increase_salary(self,percentage):
        self.salary += self.salary*percentage/100

    def display_salary(self):
        print("updated salary:",self.salary)


salary=int(input("Enter your salary:"))
percentage=float(input("enter percentage:"))

p= employee(salary)

p.increase_salary(percentage)
p.display_salary()