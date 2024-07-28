class employee:
    companyname="apple"#class variables
    def __init__(self,name):
        self.name=name
        self.raiseamount=0.02#instance variables
    def showdetails(self):
        print(f"the name of the employee is{self.name} an raise is : {self.raiseamount} and he works at {self.companyname}")
emp1=employee("rajdeep")
emp1.raiseamount=0.03
emp1.companyname="microsoft"#instance variables
emp1.showdetails()
emp2=employee("rohan")
emp2.showdetails()