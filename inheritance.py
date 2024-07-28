class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"the name of the employee is {self.name} and id is {self.id}")
class admin(employee):
    def showlang(self):
        print("the employee is using python")
object1=admin("rajdeep",400)
object1.show()
object1.showlang()
