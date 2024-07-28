class employee:
    def __init__(self):
        self.name=input("enter your name")
        self.salary=int(input("enter your salary"))
    def display(self):
     print("the name of the employee is:",self.name)
     print("the salary of the employee is:",self.salary)
obj1=employee()
obj1.display()