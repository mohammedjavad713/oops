class Employee:
    def calculate_salary(self):
        pass


class FullTime(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print("Full-time Salary =", self.salary)


class PartTime(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        print("Part-time Salary =", self.hours * self.rate)


f = FullTime(30000)
p = PartTime(80, 150)

f.calculate_salary()
p.calculate_salary()
