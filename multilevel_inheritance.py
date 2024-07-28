class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def showdetails(self):
        print(f"NAME : {self.name}")
        print(f"SPECIES : {self.species}")
class Dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="dog")
        self.breed=breed
    def showdetails(self):
        animal.showdetails(self)
        print(f"breed :{self.breed}")
class goldenret(Dog):
    def __init__(self, name,color):
        Dog.__init__(self,name,breed="golden retreiver")
        self.color=color
    def showdetails(self):
        Dog.showdetails(self)
        print(f"color :{self.color}")
obj1=goldenret("tommy","gold")
obj1.showdetails()    
