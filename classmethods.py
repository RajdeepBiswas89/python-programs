class employee:
    def __init__(self,fname,lname):
        self.first_name=fname
        self.last_name=lname
    @classmethod
    def salary(cls,salary):
        employee.sal=salary
obj1=employee("rajdeep","biswas")
employee.salary(20000000)
print(obj1.sal)

