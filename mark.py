class mark:
    def __init__(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 =mark2
        self.mark3 = mark3

    def total(self):
        return self.mark1 + self.mark2 + self.mark3
       
    def average(self):
        return self.total()/3

    def get_grade(self):
        if self.average() >= 90:
            return "A"
        elif self.average() >= 75:
            return "B"
        elif self.average() >= 50:
            return "Pass"
        else:
            return "Fail"
        
        


mark1 = int(input("Enter  the mark 1: "))
mark2 = int(input("Enter the mark 2: "))
mark3 = int(input("Enter the mark3: "))

p = mark(mark1,mark2,mark3)

# print("mark1:", self.mark1)
# print("mark2:", self.mark2)
# print("mark3:", self.mark3)
print("Total mark:",p.total())
print("average:",p.average())
print("grade:",p.get_grade())

# p.total()
# p.average()
# p.grade()