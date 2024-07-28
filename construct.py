class person:
    def __init__(self,n,o):
        print("hey, constructor called")
        self.x=n 
        self.y=o
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=person("rajdeep","machine learning enginner")
b=person("rohan","software engineer")
a.info()
b.info()

