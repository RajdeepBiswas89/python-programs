x=[1,2,4,4,5,6]
print(dir(x)) #used to see which which methods are available 
print(x.__getitem__(2))
class person:
    def __init__(self,name,age,version):
        self.name=name
        self.age=age
        self.version=version
a=person("rajdeep",20,"2.4.5")
print(a.__dict__)#gives it in a form of a dictionary

