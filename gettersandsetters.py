class employee:
    def setID(self,id):
        self.id=id
    def getID(self):
        return self.id
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
obj1=employee()
obj1.setID(221003003015)
obj1.setName("Rajdeep Biswas")
obj2=employee()
obj2.setID(221003003020)
obj2.setName("harry")
print("the name of person 1 is",obj1.getName());
print("the id of person 1 is",obj1.getID());
print("the name of person 2 is",obj2.getName())
print("the id of person 2 is",obj2.getID())
