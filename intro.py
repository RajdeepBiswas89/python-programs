class person:
    name="rajdeep"
    occupation="machine learning developer"
    salary=200000
    def info(self):
     print(f"{self.name} is a {self.occupation}")

obj1=person()#creating a object
obj2=person()
obj1.name="harry"
obj1.occupation="HR"
obj2.name="rohan"
obj2.occupation="software developer"
obj1.info()
obj2.info()
