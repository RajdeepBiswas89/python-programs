class employeee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name is {self.name}")
class dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"the dance is {self.dance}")
class DancerEmployee(dancer,employeee): #as dancer is first class so, show function for dancer is called
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name
obj=DancerEmployee("kathak","rajdeep")
obj.show()


