class magicmethods:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __repr__(self):
        return f"the name of the employee is {self.name} and his salary is {self.salary} (__repr__ method)"
    def __str__(self):
        return f"the name of the employee is {self.name} and his salary is {self.salary}"
obj1=magicmethods("rajdeep",70000)
obj2=magicmethods("harry",20000)
print(obj1)
print(obj2)
print(dir(obj1))