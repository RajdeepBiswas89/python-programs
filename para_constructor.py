class faculty:
    def __init__(self,a,b,c):
        self.name=a;
        self.id=b;
        self.salary=c;
    def display(self):
        print("the name of the employee is :",self.name)
        print("the id of the employee is : ",self.id)
        print("the monthly salary of the employee is :",self.salary)
obj=faculty("rajdeep",221003003015,90000)
obj1=faculty("rohan",500,78000)
obj.display()
obj1.display()